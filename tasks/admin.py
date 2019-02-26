from django.contrib import admin
from tasks.models import Task, TaskComment, TaskLike

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskComment)
admin.site.register(TaskLike)
