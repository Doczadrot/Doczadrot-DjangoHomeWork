from .models import Product
from django.contrib import admin
from .models import Category


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

# Register your models here.
