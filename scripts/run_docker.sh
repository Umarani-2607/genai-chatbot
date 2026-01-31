#!/bin/bash

echo "Building Docker image..."
docker build -t genai-chatbot .

echo "Running Docker container..."
docker run -it genai-chatbot
