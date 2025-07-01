# blog/admin.py

from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'contents', 'on_published', 'date_created', 'count_views')
    list_filter = ('on_published', 'date_created',)
    search_fields = ('title', 'contents')