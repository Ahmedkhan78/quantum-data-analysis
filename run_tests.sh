#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest -v --headless

# Capture exit code
EXIT_CODE=$?

# Deactivate environment
deactivate

# Return proper exit code
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed ✅"
    exit 0
else
    echo "Tests failed ❌"
    exit 1
fi