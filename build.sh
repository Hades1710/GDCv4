#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r BBM/requirements.txt

# Change to BBM directory and set Python path
cd BBM
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run collectstatic
python manage.py collectstatic --no-input

# Copy the SQLite database to the writable tmp directory if it exists
if [ -f db.sqlite3 ]; then
    mkdir -p /tmp/db
    cp db.sqlite3 /tmp/db/db.sqlite3
    # We'll set up symlink in start command
fi
