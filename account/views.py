import jwt

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.utils import timezone, dateformat
from django.contrib.auth.models import User, update_last_login

from .serializers import UserSerializer


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        update_last_login(None, user)

        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)  # many=True
            data = {
                'user': serializer.data,
                'token': auth_token
            }
            
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ActivityView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        user = User.objects.get(username=username)
        data = {
            'last_login': user.last_login
        }

        return Response(data, status=status.HTTP_200_OK)
