#!/bin/bash

set -e
cd ..

if [ ! -d ".venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv .venv
    echo "Virtual environment created."
else
    echo "Virtual environment found."
fi

echo "Activating virtual environment..."
source .venv/bin/activate

if [ ! -f "requirements.txt" ]; then
    echo "No requirements.txt found. Please generate it first."
    exit 1
fi

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running the application..."
python src/main.py

deactivate
echo "Application started successfully."