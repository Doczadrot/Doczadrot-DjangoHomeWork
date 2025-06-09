from django.urls import path
from .views import home, contact, product_list

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', product_list, name='product_list'),
]