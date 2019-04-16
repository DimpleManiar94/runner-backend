from django.shortcuts import render
from rest_framework import viewsets
from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class UserAccountView(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class UserRegistrationView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
