# Generated by Django 3.2.8 on 2022-01-11 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_from_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.IntegerField(verbose_name='Количество шагов')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('pulse', models.IntegerField(verbose_name='Пульс')),
                ('temperature', models.IntegerField(verbose_name='Температура')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edited_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Данные',
                'verbose_name_plural': 'Данные',
                'db_table': 'users data',
                'ordering': ('date',),
            },
        ),
    ]