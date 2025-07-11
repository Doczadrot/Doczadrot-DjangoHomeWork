from django.urls import path

from .views import HomeListView, ContactView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

from django.conf.urls.static import static

app_name = 'catalog'


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/create/', ProductCreateView.as_view(), name='product_create')
]