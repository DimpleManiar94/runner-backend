from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Task(models.Model):
    TASK_TYPES = (
        ('Shopping', 'Shopping'),
        ('Moving', 'Moving'),
        ('Lifting', 'Lifting'),
        ('Other', 'Other'),
    )
    TASK_STATUSES = (
        ('Available', 'Available'),
        ('Running', 'Running'),
        ('Completed', 'Completed'),
    )
    TaskTitle = models.CharField(max_length=200)
    Description = models.TextField(null=True, blank=True)
    Reward = models.IntegerField()
    DateOfCompletion = models.DateField()
    TimeOfCompletion = models.TimeField()
    Addr1 = models.CharField(max_length=200)
    Addr2 = models.CharField(max_length=200, blank=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=10)
    TaskType = models.CharField(max_length=10, choices=TASK_TYPES)
    TaskStatus = models.CharField(max_length=10, choices=TASK_STATUSES)
    AuthorFK = models.ForeignKey(UserAccount, related_name='author', on_delete=models.CASCADE, null=True)
    RunnerFK = models.ForeignKey(UserAccount, related_name='runner', on_delete=models.CASCADE, null=True, blank=True)
    CreatedTS = models.DateTimeField(auto_now_add=True)
    UpdatedTS = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.TaskTitle

class TaskComment(models.Model):
    Comment = models.CharField(max_length=1200)
    UserFK = models.ForeignKey(UserAccount, related_name='Comment_User', on_delete=models.CASCADE, null=True)
    TaskFK = models.ForeignKey(Task, related_name='Comment_Task', on_delete=models.CASCADE, null=True)
    CreatedTS = models.DateTimeField(auto_now_add=True)
    UpdatedTS = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Comment

class TaskLike(models.Model):
    UserFK = models.ForeignKey(UserAccount, related_name='Like_user', on_delete=models.CASCADE, null=True)
    TaskFK = models.ForeignKey(Task, related_name='Like_task', on_delete=models.CASCADE, null=True)



