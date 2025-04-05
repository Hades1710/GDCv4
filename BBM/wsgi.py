"""
WSGI config for bloodbankmanagement project.
"""

import os
import sys

# Add paths to ensure modules can be found
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Use the settings from bloodbankmanagement
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloodbankmanagement.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
