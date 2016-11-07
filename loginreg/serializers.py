from .models import UserProfile, User
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model= User
#         fields = ('pk', 'username', 'first_name', 'last_name', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        fields = ('role',)


class EmptySerializer(serializers.ModelSerializer):
    class Meta:
        model= UserProfile
        field=('role',)