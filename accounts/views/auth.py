from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers.auth import UserLoginSerializer
from accounts.serializers.users import UserCredentialsViewSerializer
from drf_yasg.utils import swagger_auto_schema


from accounts.swagger.auth import signup_request_body, login_response_body



class Signup(APIView):
    """регистрация нового пользователя"""

    @swagger_auto_schema(request_body=signup_request_body, responses={201: ''})
    def post(self, request):

        """
        API endpoints for posts
        """
        # создание user
        try:
            user_serializer = UserCredentialsViewSerializer(data={'email': request.data.get('email'),
                                                              'password': request.data.get('password')
                                                              })
            user_serializer.is_valid(raise_exception=True)
            user = user_serializer.create(validated_data=user_serializer.validated_data)
            user.set_password(str(request.data.get('password')))
        except IntegrityError as error:
            return Response(status=400, data={"error": error.args[1]})


class Login(APIView):
    """вход пользователя, получение токена"""

    @swagger_auto_schema(request_body=UserLoginSerializer,
                         responses={200: login_response_body})
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(data=serializer.validated_data, status=200)


class UpdateToken(APIView):
    """обновление токена текущего пользователя"""
    pass


class Logout(APIView):
    """выход текущего пользователя"""
    pass
