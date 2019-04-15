from rest_framework import serializers
from .models import Setting, UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'Phone', 'ProfilePicture', 'Addr1', 'Addr2',
                  'City', 'State', 'PostalCode')