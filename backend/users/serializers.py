from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CustomUser
        fields = "__all__"


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CustomUser
        fields = ["username", "completed", "not_completed", "date_joined", "pk"]

