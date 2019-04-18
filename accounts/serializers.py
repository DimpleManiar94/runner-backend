from builtins import setattr

from rest_framework import serializers
from .models import Setting, UserAccount, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

class UserAccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserAccount
        fields = ('user', 'Phone', 'ProfilePicture', 'Addr1', 'Addr2', 'City', 'State', 'PostalCode')

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        user = User.objects.create_user(**user_data)
        return UserAccount.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user_dict = validated_data.pop('user', None)
        if user_dict:
            user_obj = instance.user
            for key, value in user_dict.iteritems():
                setattr(user_obj, key, value)
            user_obj.save()
            validated_data["user"] = user_obj
        for key, value in validated_data.iteritems():
            setattr(instance, key, value)
        instance.save()
        return instance


    """def update(self, instance, validated_data):
       user_dict = validated_data.pop('user', None)
       if user_dict:
           user_obj = instance.user
           for key, value in user_dict.iteritems():
                setattr(user_obj, key, value)
           user_obj.save()
           validated_data["user"] = user_obj
       for key, value in validated_data.iteritems():
           setattr(instance, key, value)
       instance.save()
       return instance"""