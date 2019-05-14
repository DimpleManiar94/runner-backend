from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, TaskComment
from .serializers import TaskSerializer, TaskCommentSerializer

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    #queryset = Task.objects.all().order_by('-CreatedTS')
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all().order_by('-CreatedTS')
        status = self.request.query_params.get('status', None)
        author = self.request.query_params.get('author', None)
        runner = self.request.query_params.get('runner', None)
        category = self.request.query_params.get('category', None)
        if status is not None:
            queryset = queryset.filter(TaskStatus=status)
        if author is not None:
            queryset = queryset.filter(AuthorFK=author)
        if runner is not None:
            queryset = queryset.filter(RunnerFK=runner)
        if category is not None:
            queryset = queryset.filter(TaskType=category)
        return queryset

class TaskCommentView(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
