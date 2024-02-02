# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Pipenv files into the container
COPY Pipfile Pipfile.lock ./

# Install dependencies
# We first install pipenv and then use it to install the rest of the dependencies
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy

# Copy the rest of your application's code
COPY . .

# You may add commands to copy .env from .env.sample or use environment variables
# COPY .env.sample .env
# Or configure environment variables in your Docker command or docker-compose.yml

# Command to run the application
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]