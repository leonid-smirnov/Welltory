"""Описание моделей для БД"""
import numpy as np
from django.conf import settings
from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver


class Data_from_users(models.Model):
    """Класс модели данных от пользователей в БД, описание полей"""
    id = models.AutoField  # Идентификатор строки

    title = models.CharField(
        max_length=20,
        verbose_name='Название',
        editable=True,
        null=False,
        blank=True,
    )  # Название

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )  # внешний ключ на таблицу User

    date_steps = models.DateField(
        verbose_name='Дата создания',
        editable=True,
        null=False,
    )  # Дата внесения значений

    steps = models.FloatField(
        verbose_name='Количество шагов',
        null=False,
        blank=True,
    )  # Данные значений шагов

    date_pulse = models.DateField(
        verbose_name='Дата создания',
        editable=True,
        null=False,
    )  # Дата внесения значений

    pulse = models.FloatField(
        verbose_name='Пульс',
        null=False,
        blank=True,
    )  # Пульс

    date_temperature = models.DateField(
        verbose_name='Дата создания',
        editable=True,
        null=False,
    )  # Дата внесения значений

    temperature = models.FloatField(
        verbose_name='Температура',
        null=False,
        blank=True,
    )  # Температура

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        editable=False,
        null=False,
        blank=False,
    )  # Дата создания

    edited_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
        editable=False,
        null=False,
        blank=False,
    )  # Дата изменения

    Pearson_count = models.FloatField(
        max_length=30,
        blank=True,
        default=None,
        null=False,
    )  # Расчетное значение Пирсона

    class Meta:
        """Мета класс модели - название, сортировка"""
        db_table = 'users_data'
        ordering = ("created_at",)  # Сортировка по дате создания
        verbose_name = "Данные"
        verbose_name_plural = "Данные"

    @property
    def pearson(self):
        """ Функция расчета Коэффициента корреляции Пирсона """

        date_steps = Data_from_users.objects.filter()
        date_steps_v = date_steps.values_list('date_steps')
        date_steps = np.array(date_steps_v)

        date_pulse = Data_from_users.objects.filter()
        date_pulse_v = date_pulse.values_list('date_pulse')
        date_pulse = np.array(date_pulse_v)

        pk = Data_from_users.objects.filter()
        pk_v = pk.values_list('pk')
        pk = np.array(pk_v)

        pulse = Data_from_users.objects.filter()
        pulse_v = pulse.values_list('pulse')
        pulse = np.array(pulse_v)

        steps = Data_from_users.objects.filter()
        steps_v = steps.values_list('steps')
        steps = np.array(steps_v)

        calc_pulse = []
        steps_calc = []

        for date_s in date_steps:
            for date_p in date_pulse:
                if date_s == date_p:

                    for i in range(0, len(pk)):

                        if pulse[i] > 0 and steps[i] > 0:

                            calc_pulse = np.append(calc_pulse, pulse[i], axis=0)
                            steps_calc = np.append(steps_calc, steps[i], axis=0)

                            Pearson_count = np.corrcoef(calc_pulse, steps_calc, rowvar=False)[0, 1]

                        else:
                            pass
                else:
                    pass

        return Pearson_count


@receiver(pre_save, sender=Data_from_users)
def calc_pearson_total(sender, instance, **kwargs):
    """Функция переопределения метода save() модели для записи расчетного поля
    (Коэффициента корреляции Пирсона) в БД"""
    instance.Pearson_count = instance.pearson


def __str__(self):
    return self.title
