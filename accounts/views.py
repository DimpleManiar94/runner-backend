from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAccount, User
from .serializers import UserAccountSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class UserAccountView(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserRegistrationView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

