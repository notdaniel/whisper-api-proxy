from io import BytesIO
import httpx
from rich.console import Console
from starlette.applications import Starlette
from starlette.config import Config
from starlette.datastructures import Secret
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse
from starlette.routing import Route

config = Config(".env")
console = Console()

HOST: str = config("HOST", cast=str, default="0.0.0.0")
PORT: int = config("PORT", cast=int, default=8000)
DEBUG: bool = config("DEBUG", cast=bool, default=False)
OPENAI_API_KEY = Secret = config("OPENAI_API_KEY", cast=Secret)


async def transcribe(data: bytes) -> str:
    file = ("audio.m4a", BytesIO(data), "audio/m4a")

    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.openai.com/v1/audio/transcriptions",
            files={"file": file},
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            data={"model": "whisper-1"},
        )
    transcript = r.json()
    return transcript["text"]


async def handle_index(request: Request) -> JSONResponse:
    rv = {"hello": "world"}
    return JSONResponse(rv)


async def handle_transcribe(request: Request) -> PlainTextResponse:
    upload: bytes = await request.body()
    console.log(f"Received {len(upload)} bytes")

    transcription = await transcribe(upload)
    console.log(f'Transcription: "{transcription}"')

    return PlainTextResponse(transcription)


routes = [
    Route("/", handle_index),
    Route("/transcribe", handle_transcribe, methods=["POST"]),
]

app = Starlette(routes=routes, debug=DEBUG)
