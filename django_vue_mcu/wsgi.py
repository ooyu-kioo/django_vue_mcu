"""
WSGI config for django_vue_mcu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# WSGIインターフェースに対応したアプリサーバーからこのプロジェクトを呼び出すときのエントリーポイント

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_vue_mcu.settings')

application = get_wsgi_application()
