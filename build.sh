#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r BBM/requirements.txt

# Ensure our BBM module can be imported
touch BBM/__init__.py

# Make sure the database directory exists
mkdir -p /tmp/db

# Copy database if needed
if [ -f BBM/db.sqlite3 ]; then
    cp BBM/db.sqlite3 /tmp/db/db.sqlite3
fi

# Create a simple test to verify our approach
echo "Testing Django settings import..."
cd BBM
python -c "import sys; print(sys.path); import os; print(os.getcwd()); from bloodbankmanagement import settings; print('Settings import successful!')"
echo "Import test completed."
