from rest_framework import serializers
from welltory_test.models import Data_from_users


class DataUserSerializer(serializers.ModelSerializer):  # Сериалайзер для таблицы Data от клиентов

    class Meta:
        model = Data_from_users
        fields = ('id',
                  'user',
                  'title',
                  'date_steps',
                  'steps',
                  'date_pulse',
                  'pulse',
                  'date_temperature',
                  'temperature',
                  'Pearson_count',
                  'created_at',
                  'edited_at',
                  )


class DataUserSerializerTest(serializers.ModelSerializer):  # Сериалайзер для таблицы Data от клиентов

    date_steps = serializers.DateField(label='Дата шагов')
    steps = serializers.IntegerField(label='Количество шагов', required=True)
    # date_pulse = serializers.DateField(label='Дата пульс')
    # pulse = serializers.IntegerField(label='Пульс', required=True)
    # date_temperature = serializers.DateField(label='Дата температура')
    # temperature = serializers.IntegerField(label='Пульс', required=True)

    class Meta:
        model = Data_from_users
        fields = ('user',
                  'date_steps',
                  'steps',
                  # 'date_pulse',
                  # 'pulse',
                  # 'date_temperature',
                  # 'temperature',
                  )


