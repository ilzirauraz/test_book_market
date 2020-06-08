from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'auth_token']

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class AuthorSerializer(serializers.Serializer):
    fio = serializers.CharField(max_length=255)


class BookSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()


class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = ['username', 'user_phone', 'comment']

    def create(self, validated_data):
        return PurchaseRequest.objects.create(**validated_data)
