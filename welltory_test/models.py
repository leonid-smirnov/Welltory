from django.conf import settings
from django.db import models
import numpy as np

'''Модель переданных данных от пользователей в БД'''


class Data_from_users(models.Model):
    id = models.AutoField  # Идентификатор строки
    title = models.CharField(max_length=20, verbose_name='Название', editable=True, null=False, blank=True, default='Мои данные')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь',
                             on_delete=models.CASCADE)  # внешний ключ на таблицу User

    date_steps = models.DateField(verbose_name='Дата создания', editable=True, null=False, )  # Дата внесения значений
    steps = models.FloatField(verbose_name='Количество шагов', null=False, blank=True, )  # Данные значений шагов
    date_pulse = models.DateField(verbose_name='Дата создания', editable=True, null=False, )  # Дата внесения значений
    pulse = models.FloatField(verbose_name='Пульс', null=False, blank=True, )  # Пульс
    date_temperature = models.DateField(verbose_name='Дата создания', editable=True,
                                        null=False, )  # Дата внесения значений
    temperature = models.FloatField(verbose_name='Температура', null=True, blank=True, )  # Температура

    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, editable=False, null=False,
                                      blank=False)  # Дата создания
    edited_at = models.DateTimeField(verbose_name='Дата изменения', auto_now_add=True, editable=False, null=False,
                                     blank=False)  # Дата изменения

    Pearson_count = models.FloatField(max_length=30, blank=True, null=True, default=None)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'users_data'
        ordering = ("created_at",)  # Сортировка по дате создания
        verbose_name = "Данные"
        verbose_name_plural = "Данные"

    def save(self, *args, **kwargs):
        self.Pearson_count = self.Pearson_count
        super(Data_from_users, self).save(*args, **kwargs)
