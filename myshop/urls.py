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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls'))
]
