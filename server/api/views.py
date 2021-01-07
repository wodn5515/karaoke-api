from django.shortcuts import render
from rest_framework import viewsets
from todo.models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodoViewset(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def create(self, request, **kwargs):
        serializers = TodoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(author=request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_active:
            return Todo.objects.filter(author=user)
        else:
            return None
