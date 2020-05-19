from django.contrib.auth.models import User
from rest_framework import serializers

from .models import History


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        

class UserDetailSerializer(serializers.ModelSerializer):
    histories = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'histories']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['query', 'created_at']


