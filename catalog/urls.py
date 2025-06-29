from django.urls import path

from .views import HomeListView, ContactView, ProductDetailView, ProductListView

from django.conf.urls.static import static


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
]