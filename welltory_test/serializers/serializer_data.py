from rest_framework import serializers
from welltory_test.models import Data_from_users


class Data_User_Serializer(serializers.ModelSerializer):  # Сериалайзер для таблицы Data от клиентов
    class Meta:
        model = Data_from_users
        fields = (
                  'user_id',
                  'steps',
                  'date',
                  'pulse',
                  'temperature',
                  'created_at',
                  'edited_at',
                                    )
