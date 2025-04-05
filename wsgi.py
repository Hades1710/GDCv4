"""
WSGI config for bloodbankmanagement project.

This file deliberately mimics the location and structure of the original WSGI file
to help Render find it during deployment.
"""

import os
import sys

# Add system paths to ensure modules can be found
sys.path.append('/opt/render/project/src')
sys.path.append('/opt/render/project/src/BBM')

# Define the WSGI application using the absolute settings module path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bloodbankmanagement.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
