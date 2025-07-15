
from users.forms import UsersRegisterForm
from users.models import Users
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

class UserRegisterView(CreateView):
    model = Users
    form_class = UsersRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Сначала вызываем родительский метод, чтобы сохранить нового пользователя в базе данных
        response = super().form_valid(form)
        user = self.object
        subject = 'Добро пожаловать в SkyStore!'
        message = (
            f'Здравствуйте, {user.email}!\n\n'
            'Мы рады приветствовать вас в нашем магазине SkyStore.\n'
            'Спасибо за регистрацию! Мы надеемся, что вам понравится пользоваться нашим сервисом.\n\n'
            'С уважением,\nКоманда SkyStore'
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return response


