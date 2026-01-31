#!/bin/bash

echo "Simulating CI pipeline..."

echo "Step 1: Build Docker image"
docker build -t genai-chatbot .

echo "CI simulation completed successfully."
