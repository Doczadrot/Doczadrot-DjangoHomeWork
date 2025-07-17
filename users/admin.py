# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
from .forms import UsersRegisterForm, UsersChangeForm
@admin.register(Users)
class CustomUserAdmin(UserAdmin):

    # Форма для создания нового пользователя (используется create_superuser)
    add_form = UsersRegisterForm
    # Форма для изменения существующего пользователя
    form = UsersChangeForm

    list_display = ('email', 'phone_number', 'is_staff', 'is_active')
    search_fields = ('email', 'phone_number',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # Определяем наборы полей для отображения и редактирования пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('phone_number', 'image', 'country')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2'), # password2 для подтверждения пароля
        }),
        ('Персональная информация', {'fields': ('phone_number', 'image', 'country')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    # Указываем поле, которое является USERNAME_FIELD
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
