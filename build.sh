#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r BBM/requirements.txt

cd BBM
python manage.py collectstatic --no-input

# Copy the SQLite database to the writable tmp directory if it exists
if [ -f db.sqlite3 ]; then
    mkdir -p /tmp/db
    cp db.sqlite3 /tmp/db/db.sqlite3
    # We'll set up symlink in start command
fi
