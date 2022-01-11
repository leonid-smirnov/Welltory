from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from welltory_test.models import Data_from_users
from drf_yasg.utils import swagger_auto_schema
from welltory_test.serializers.serializer_data import Data_User_Serializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
@swagger_auto_schema(responses={200: Data_User_Serializer})
def get_data_list(request):
    if request.method == 'GET':
        Data_list = Data_from_users.objects.all()

        user = request.query_params.get('user', None)
        if user is not None:
            Data_list = Data_list.filter(user__icontains=user)

        Data_list_serializer = Data_User_Serializer(Data_list, many=True)
        return JsonResponse(Data_list_serializer.data, safe=False)

    elif request.method == 'POST':
        Data_list = JSONParser().parse(request)
        Data_list_serializer = Data_User_Serializer(data=Data_list)
        if Data_list_serializer.is_valid():
            Data_list_serializer.save()
            return JsonResponse(Data_list_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Data_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Data_from_users.objects.all().delete()
        return JsonResponse({'message': '{} Data were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
