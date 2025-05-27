from django.shortcuts import render
from django.http import HttpResponse 


def home(request):
    """
    Функция представления для отображения главной страницы.

    Args:
        request: Объект HTTP-запроса.

    Returns:
        Отрендеренный шаблон index.html.
    """
    return render(request, 'index.html')


def contact(request):
    """
    Функция представления для отображения страницы контактов.

    Args:
        request: Объект HTTP-запроса.

    Returns:
        Отрендеренный шаблон contact.html.
    """
    return render(request, 'contact.html')