from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from accounts.models import User
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'password2')

    def validate(self, attrs):
        if not attrs['password'] == attrs['password2']:
            raise serializers.ValidationError(("Пароли не совпадают"))
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        Token.objects.create(user=user)
        return validated_data
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError("Неверный email или пароль")
        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key, "email":user.email}