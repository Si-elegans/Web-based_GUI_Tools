"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

print >> sys.stderr, sys.path 
