from django.core.cache import cache
from myshop.settings import CACHE_ENABLED
from catalog.models import Product, Category


def get_product_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set('product_list', products, timeout=60 * 15)
    return products


def get_products_category(category_id):  # Обратите внимание на название функции

    if not CACHE_ENABLED:
        # Если кеширование отключено, получаем напрямую из БД
        category = Category.objects.get(pk=category_id)
        return Product.objects.filter(category=category, is_published=True).order_by('name')
    else:

        key = f"category_products_{category_id}"

        products_from_cache = cache.get(key)

        if products_from_cache is not None:
            return products_from_cache  # Возвращаем из кеша, если найдено

        # Если в кеше нет, получаем данные из базы данных
        category = Category.objects.get(pk=category_id)
        products = Product.objects.filter(category=category, is_published=True).order_by('name')

        cache.set(key, products, timeout=60 * 15)

        return products
