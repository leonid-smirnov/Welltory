from django.contrib import admin
from django.contrib.admin import ModelAdmin
from welltory_test.models import Data_from_users


@admin.register(Data_from_users)
class User_data(ModelAdmin):
    fields = ('user', 'date', 'steps', 'pulse', 'temperature')
    list_display = ('user', 'date', 'steps', 'pulse', 'temperature')
    readonly_fields = ('created_at', 'edited_at')
