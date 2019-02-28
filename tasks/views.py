from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, TaskComment
from .serializers import TaskSerializer, TaskCommentSerializer

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCommentView(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
