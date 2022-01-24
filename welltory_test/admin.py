from django.contrib import admin
from django.contrib.admin import ModelAdmin

from welltory_test.models import Data_from_users
import numpy as np


@admin.register(Data_from_users)
class User_data(ModelAdmin):
    fields = ('user', 'title', 'date_steps', 'steps', 'date_pulse', 'pulse', 'date_temperature', 'temperature')
    list_display = (
        'user', 'title', 'date_steps', 'steps', 'date_pulse', 'pulse', 'date_temperature', 'temperature', 'pearson')
    readonly_fields = ('created_at', 'edited_at')

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.date_steps = None
        self.date_pulse = None
        self.Pearson_count = None

    def pearson(self, Pearson_count):

        # self.Pearson_count = Pearson_count
        # date_steps = self.date_steps
        # date_pulse = self.date_pulse

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



        for i in pk - 19:

            if date_steps[i] == date_pulse[i] and pulse[i] > 0 and steps[i] > 0:
                calc_pulse = np.append(calc_pulse, pulse[i])
                steps_calc = np.append(steps_calc, steps[i])

                Pearson_count = np.corrcoef(calc_pulse, steps_calc, rowvar=False)[0, 1]

        return Pearson_count
