from django.contrib import admin
from core.models import Board, Task, TaskComment, TaskAssignedUser, Message

# Register your models here.
admin.site.register(Board)
admin.site.register(Task)
admin.site.register(TaskComment)
admin.site.register(TaskAssignedUser)
admin.site.register(Message)
