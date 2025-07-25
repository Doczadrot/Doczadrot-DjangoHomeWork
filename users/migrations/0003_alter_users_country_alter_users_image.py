# Generated by Django 5.2.1 on 2025-07-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(blank=True, help_text='Введите страну проживания', null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatar/', verbose_name='AVATAR'),
        ),
    ]
