from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import History


class UserSerializer(serializers.ModelSerializer):
    histories = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'histories']


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['query', 'created_at']


