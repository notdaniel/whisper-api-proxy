whisper-api-proxy
===================

## Setup

* Install dependencies with `pipenv install`.
* Copy `.env.sample` to `.env` and save your OpenAI API key. (Setting it to envvar `OPENAI_API_KEY` is fine, too.)

## Running

* Start the server via `pipenv run serve`. (Or run `pipenv run uvicorn main:app --host 0.0.0.0`)
* Make a `POST` request to `/transcribe` containing the raw audio data. You will be returned the transcription in plaintext.

You can also quickly deploy on Render using this button.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/notdaniel/whisper-api-proxy)
