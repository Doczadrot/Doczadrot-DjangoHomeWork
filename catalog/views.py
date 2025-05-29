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
    return render(request, 'catalog/home.html')


def contact(request):
    """
    Функция представления для отображения страницы контактов.

    Args:
        request: Объект HTTP-запроса.

    Returns:
        Отрендеренный шаблон contact.html.
    """
    context = {}
    # Если это POST-запрос, значит пользователь отправил форму
    if request.method == 'POST':
        # Вы можете выполнить дополнительные действия с данными
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Создаем пустой словарь для контекста шаблона
        

        errors =  [] #Проверка полей
        if not name:
            errors.append('Имя не может быть пустым')
        if not phone:
            errors.append('Телефон не может быть пустым')
        if not message:
            errors.append('Сообщение не может быть пустым')

        if errors:
            context['errors'] = errors # Добавляем список ошибок в контекст
            return render(request, 'catalog/contact.html', context) # Возвращаем шаблон с контекстом
        return render(request, 'catalog/success.html', 
            {'name': name,
            'message': 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.'})


     # Для GET-запроса просто отображаем форму с пустым контекстом
    return render(request, 'catalog/contact.html', context)