from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    color = serializers.CharField()

    class Meta:
        model = Tag
