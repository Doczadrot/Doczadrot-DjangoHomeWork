from django.urls import path
from .views import home, contact  # Добавь импорт представлений

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]