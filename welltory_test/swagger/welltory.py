from drf_yasg import openapi

welltory_request_params = [
    openapi.Parameter('id',
                      in_=openapi.IN_QUERY,
                      type=openapi.TYPE_INTEGER,
                      description='id',
    )
]

welltory_schema = openapi.Schema(type=openapi.TYPE_OBJECT,
                                         properties={
                                             'id': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                     description='id'),
                                             'title': openapi.Schema(type=openapi.TYPE_STRING,
                                                                     description='Название'),
                                             'user': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                     description='id пользователя'),
                                             'date_steps': openapi.Schema(type=openapi.TYPE_STRING,
                                                                     description='дата шагов'),
                                             'steps': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                     description='количество шагов'),
                                             'date_pulse': openapi.Schema(type=openapi.TYPE_STRING,
                                                                          description='дата пульс'),
                                             'pulse': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                     description='количество пульс'),
                                             'date_temperature': openapi.Schema(type=openapi.TYPE_STRING,
                                                                          description='дата температура'),
                                             'temperature': openapi.Schema(type=openapi.TYPE_INTEGER,
                                                                     description='температура'),
                                         }
)
