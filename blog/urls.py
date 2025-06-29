from django.urls import path

from catalog.urls import urlpatterns
from .views import BlogListView, BlogDetailView, BlogCreateView, UpdateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='blog_delete'),
]