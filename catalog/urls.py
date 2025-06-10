from django.urls import path
from .views import home, contact, product_list
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', product_list, name='product_list'),
]