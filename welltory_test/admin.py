""" Imports and registration models for admin panel """
from welltory_test.models import Data_from_users
from django.contrib import admin
from django.contrib.admin import ModelAdmin


@admin.register(Data_from_users)
class User_data(ModelAdmin):
    fields = (
        'user',
        'title',
        'date_steps',
        'steps',
        'date_pulse',
        'pulse',
        'date_temperature',
        'temperature',
    )

    list_display = (
        'user',
        'title',
        'date_steps',
        'steps',
        'date_pulse',
        'pulse',
        'date_temperature',
        'temperature',
        'pearson',
    )

    readonly_fields = (
        'created_at',
        'edited_at',
    )
