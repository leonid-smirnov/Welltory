from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from requests import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

from accounts.models import User
from welltory_test.models import Data_from_users
from drf_yasg.utils import swagger_auto_schema
from welltory_test.serializers.serializer_data import Data_User_Serializer
from rest_framework.decorators import api_view

'''Методы для полного получения/передачи/удаления информации'''

@api_view(['GET', 'POST', 'DELETE'])
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

'''Методы для получения/обновления/удаления информации по идентификатору строки'''

@api_view(['GET', 'PUT', 'DELETE'])
def get_data_detail(request, user_id):
    try:
        Data_list = Data_from_users.objects.get(user=user_id)
    except Data_from_users.DoesNotExist:
        return JsonResponse({'message': 'Data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Data_list_serializer = Data_User_Serializer(Data_list)
        return JsonResponse(Data_list_serializer.data)

    elif request.method == 'PUT':
        Data_list = JSONParser().parse(request)
        Data_list_serializer = Data_User_Serializer(Data_list, data=Data_list)
        if Data_list_serializer.is_valid():
            Data_list_serializer.save()
            return JsonResponse(Data_list_serializer.data)
        return JsonResponse(Data_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Data_list.delete()
        return JsonResponse({'message': 'Data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

'''Методы для получения/обновления/удаления информации по user ID'''















# @api_view(['GET', 'PUT', 'DELETE'])
# def get_user_data_all(request):
#     try:
#         Data_list1 = Data_from_users.objects.all(user=request.user)
#     except Data_from_users.DoesNotExist:
#         return JsonResponse({'message': 'User data does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         Data_list_serializer = Data_User_Serializer(Data_list1)
#         return JsonResponse(Data_list_serializer.data)
#
#     elif request.method == 'PUT':
#         Data_list1 = JSONParser().parse(request)
#         Data_list_serializer = Data_User_Serializer(Data_list1, data=Data_list1)
#         if Data_list_serializer.is_valid():
#             Data_list_serializer.save()
#             return JsonResponse(Data_list_serializer.data)
#         return JsonResponse(Data_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         Data_list1.delete()
#         return JsonResponse({'message': 'User data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
