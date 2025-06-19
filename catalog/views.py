from django.shortcuts import render
from django.http import HttpResponse 
from catalog.models import Product
from django.shortcuts import render, get_object_or_404


def home(request):
    """
    Функция представления для отображения главной страницы.

    Args:
        request: Объект HTTP-запроса.

    Returns:
        Отрендеренный шаблон index.html.
    """
    context = {} # Создаем пустой словарь для контекста шаблона
    # Получаем все продукты из базы данных
    context['products'] = Product.objects.all() # Добавляем продукты в контекст

    return render(request, 'catalog/home.html', context)



def contact(request):
    """
    Функция представления для отображения страницы контактов.

    Args:
        request: Объект HTTP-запроса.

    Returns:
        Отрендеренный шаблон contact.html.
    """
    context = {}

    if request.method == 'POST':
    
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
    
        

        errors =  [] #Проверка полей
        if not name:
            errors.append('Имя не может быть пустым')
        if not phone:
            errors.append('Телефон не может быть пустым')
        if not message:
            errors.append('Сообщение не может быть пустым')

        if errors:
            context['errors'] = errors # Добавляем список ошибок в контекст
            return render(request, 'catalog/contact.html', context)
        return render(request, 'catalog/success.html', 
            {'name': name,
            'message': 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.'})

    return render(request, 'catalog/contact.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})