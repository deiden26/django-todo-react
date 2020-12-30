from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField()

    class Meta:
        model = Todo
