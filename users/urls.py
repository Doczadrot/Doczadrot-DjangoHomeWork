
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import UserRegisterView
from django.contrib.auth import views as auth_views

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register')
]