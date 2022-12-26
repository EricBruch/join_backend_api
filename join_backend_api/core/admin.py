from django.contrib import admin
from core.models import Board, Task, TaskComments, TaskUserAssignedMapping

# Register your models here.
admin.site.register(Board)
admin.site.register(Task)
admin.site.register(TaskComments)
admin.site.register(TaskUserAssignedMapping)
