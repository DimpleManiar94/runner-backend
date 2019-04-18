from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAccount, User
from .serializers import UserAccountSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics

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

