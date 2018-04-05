from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, style={'placeholder': 'User Name'})
    password = serializers.CharField(max_length=100, style={'input_type': 'password', 'placeholder': 'Password'})


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password', 'mobile_no', 'address')

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerialzer(serializers.Serializer):
    old_password = serializers.CharField(required=True, style={'input_type': 'password'})
    new_password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate_new_password(self, value):
        validate_password(value)
        return value