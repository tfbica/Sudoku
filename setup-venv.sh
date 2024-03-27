#!/bin/bash

# Define the name of the virtual environment directory
VENV_DIR=".venv"

# Check if the virtual environment directory already exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    # Create a virtual environment
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
fi

# Activate the virtual environment
if [ -f "$VENV_DIR/Scripts/activate" ]; then
    # Windows
    source "$VENV_DIR/Scripts/activate"
elif [ -f "$VENV_DIR/bin/activate" ]; then
    # macOS and Linux
    source "$VENV_DIR/bin/activate"
else
    echo "Failed to activate virtual environment. Please activate it manually."
fi

# Install dependencies from requirements.txt (if exists)
if [ -f "requirements.txt" ]; then
    $VENV_DIR/bin/pip3 install -r requirements.txt
    echo "Dependencies installed from requirements.txt."
fi

echo "Virtual environment setup complete."
