"""
Конфигурация URL для проекта myshop.

Список `urlpatterns` направляет URL к представлениям. Документация:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Примеры:
Функциональные представления
    1. Импорт: from my_app import views
    2. Добавить URL: path('', views.home, name='home')
Класс-базированные представления
    1. Импорт: from other_app.views import Home
    2. Добавить URL: path('', Home.as_view(), name='home')
Включение других URLconf
    1. Импорт функции include: from django.urls import include, path
    2. Добавить URL: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
