from django import forms
from users.models import Users
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsersRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('email',)

class UsersChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ('email', 'phone_number', 'image', 'country', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions') # Включите все поля, которые хотите редактировать


