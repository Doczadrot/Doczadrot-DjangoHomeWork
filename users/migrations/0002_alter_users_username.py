# Generated by Django 5.2.1 on 2025-07-13 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
