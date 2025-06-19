from django.urls import path

from .views import home, contact, product_detail, product_list

from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),]