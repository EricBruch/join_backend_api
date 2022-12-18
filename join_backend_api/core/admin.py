from django.contrib import admin
from core.models import Board, Task, TaskCommentsMapping, TaskUserAssignedMapping

# Register your models here.
admin.site.register(Board)
admin.site.register(Task)
admin.site.register(TaskCommentsMapping)
admin.site.register(TaskUserAssignedMapping)
