import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product # Импортируем модели

class Command(BaseCommand):
    help = 'Загружает начальные тестовые данные (категории и продукты) в базу данных.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Начинаем загрузку начальных данных...'))

        # Удаляем все существующие данные (для чистого состояния)
        self.stdout.write('Удаление существующих продуктов и категорий...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Существующие данные удалены.'))

        # Загружаем данные из фикстур
        self.stdout.write('Загрузка фикстур categories.json и products.json...')
        try:
            call_command('loaddata', 'categories.json')
            call_command('loaddata', 'products.json')
            self.stdout.write(self.style.SUCCESS('Фикстуры успешно загружены!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при загрузке фикстур: {e}'))

        self.stdout.write(self.style.SUCCESS('Процесс загрузки начальных данных завершен.'))