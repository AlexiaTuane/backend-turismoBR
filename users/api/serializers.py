# users/serializers.py
from rest_framework import serializers
from users.models import CustomUser 

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'is_active', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}