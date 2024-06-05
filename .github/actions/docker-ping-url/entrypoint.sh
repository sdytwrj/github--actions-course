#!/bin/bash

# Set input arguments as environment variables
export URL=$1
export MAX_TRIALS=$2
export DELAY=$3

# Run your Python script
python /app/main.py
