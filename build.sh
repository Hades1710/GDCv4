#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r BBM/requirements.txt

# Create a symbolic link to make the module structure work
mkdir -p /opt/render/project/src/bloodbankmanagement
touch /opt/render/project/src/bloodbankmanagement/__init__.py
ln -sf /opt/render/project/src/BBM/bloodbankmanagement/settings.py /opt/render/project/src/bloodbankmanagement/
ln -sf /opt/render/project/src/BBM/bloodbankmanagement/wsgi.py /opt/render/project/src/bloodbankmanagement/
ln -sf /opt/render/project/src/BBM/bloodbankmanagement/urls.py /opt/render/project/src/bloodbankmanagement/

# Copy database if needed
if [ -f BBM/db.sqlite3 ]; then
    mkdir -p /tmp/db
    cp BBM/db.sqlite3 /tmp/db/db.sqlite3
fi
