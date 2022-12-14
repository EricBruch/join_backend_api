from rest_framework import serializers
from .models import Board

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title', 'created_at']