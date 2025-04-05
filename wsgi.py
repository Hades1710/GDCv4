"""
WSGI config for bloodbankmanagement project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments.
"""

import os
import sys

# Add the BBM directory to the Python path
base_dir = os.path.dirname(os.path.abspath(__file__))
bbm_dir = os.path.join(base_dir, 'BBM')
sys.path.append(bbm_dir)

# Define the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloodbankmanagement.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
