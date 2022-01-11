from django.conf import settings
from django.db import models

'''Модель переданных данных от пользователей в БД'''

class Data_from_users(models.Model):

    id = models.AutoField  # Идентификатор строки
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь',
                             on_delete=models.CASCADE)  # внешний ключ на таблицу User
    steps = models.FloatField(verbose_name='Количество шагов', null=True, blank=True, )  # Данные значений шагов

    date = models.DateTimeField(verbose_name='Дата создания', editable=True, null=False, )  # Дата внесения значений

    pulse = models.FloatField(verbose_name='Пульс', null=True, blank=True, )  # Пульс

    temperature = models.FloatField(verbose_name='Температура', null=True, blank=True, )  # Температура

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, editable=False, null=False,
                                      blank=False)  # Дата создания
    edited_at = models.DateTimeField(verbose_name='Дата изменения', auto_now_add=True, editable=False, null=False,
                                     blank=False)  # Дата изменения

    class Meta:
        db_table = 'users data'
        ordering = ("date",)  # Сортировка по дате
        verbose_name = "Данные"
        verbose_name_plural = "Данные"
