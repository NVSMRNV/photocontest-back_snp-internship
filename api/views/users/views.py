from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import APIView

from models_app.models.user.models import User
from api.serializers.users.seriailizers import UserSerializer

from drf_yasg.utils import swagger_auto_schema
from api.docs.users.login import LOGIN_PARAMETERS
from api.docs.users.register import REGISTER_PARAMETERS


class RegisterUserAPIView(APIView):
    parser_classes = [JSONParser]

    @swagger_auto_schema(**REGISTER_PARAMETERS)
    def post(self, request: HttpRequest, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(APIView):
    parser_classes = [JSONParser]

    @swagger_auto_schema(**LOGIN_PARAMETERS)
    def post(self, request: HttpRequest, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response({'error': 'Пользователь не найден.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Неверный пароль.'}, status=status.HTTP_400_BAD_REQUEST)
        