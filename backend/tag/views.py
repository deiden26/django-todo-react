
# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TagSerializer
from .models import Tag

class TodoView(viewsets.ModelViewSet):
  serializer_class = TagSerializer
  queryset = Tag.objects.all()
