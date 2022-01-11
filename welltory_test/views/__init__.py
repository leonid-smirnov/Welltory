from django.db import models
from django.utils.timezone import now

from accounts.models import User

class Processing_data(models.Model):
    """Данные от пользователей с frontend для обработки"""

    name = models.CharField(
        primary_key=True,
        db_index=True,
        max_length=200,
        verbose_name="Имя пользователя",
    )

