"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/

이 파일은 Gunicorn과 같은 WSGI서버에서 호출하는 장고의 WSGI 애플리케이션이다.
WSGI 서버는 항상 이 파일을 호출하여 장고(django) 프로그램을 실행한다.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
