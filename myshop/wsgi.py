"""
WSGI конфигурация для проекта myshop.

Предоставляет вызываемый WSGI объект как переменную уровня модуля с именем ``application``.

Дополнительная информация:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

application = get_wsgi_application()
