from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication

from django.contrib.auth.models import User

from knox.models import AuthToken

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer
)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)[1]
        # nested serializer
        return Response({
            "user": UserSerializer(user,
            context=self.get_serializer_context()).data,
            "token": token
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny,]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        # nested serializer
        return Response({
            "user": UserSerializer(user,
            context=self.get_serializer_context()).data,
            "token": token
        })


class UserAPI(generics.RetrieveAPIView):
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        print(self.request.user)
        return self.request.user
