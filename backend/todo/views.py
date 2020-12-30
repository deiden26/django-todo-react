from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TodoSerializer
from .filters import TodoFilterset
from .models import Todo

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    filterset_class = TodoFilterset
    queryset = (Todo.objects.all()
                .prefetch_related('tags'))

    @action(detail=True, methods=['post'])
    def capitalize_title(self, request):
        todo = self.get_object()
        todo.title.capitalize()
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data)
