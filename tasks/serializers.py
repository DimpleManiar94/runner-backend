from rest_framework import serializers
from .models import Task, TaskLike, TaskComment

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'TaskTitle', 'Description', 'Reward', 'DateOfCompletion', 'TimeOfCompletion', 'Addr1', 'Addr2',
                  'City', 'State', 'PostalCode', 'TaskType', 'TaskStatus', 'AuthorFK', 'RunnerFK', 'CreatedTS',
                  'UpdatedTS')

class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id','Comment', 'UserFK', 'TaskFK', 'CreatedTS', 'UpdatedTS')