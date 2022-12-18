from django.db import models
# import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.utils.timezone import now

# class Status(models.TextChoices):
#     BACKLOG = 'BL'
#     TO_DO = 'TD'

User = get_user_model()

Urgency = models.TextChoices('Urgency', ['URGENT', 'MEDIUM', 'LOW'])

Status = models.TextChoices(
    'Status', ['BACKLOG', 'TO_DO', 'IN_PROGRESS', 'REVIEW', 'DONE']
)


class Board(models.Model):
    title = models.CharField(max_length=100, default='')
    created_at = models.DateField(default=now())


class Task(models.Model):
    title = models.CharField(max_length=100, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=300, default='')
    due_date = models.DateField(
        default=(now() + relativedelta(months=+3))
    )
    created_at = models.DateField(default=now())
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE
    )

    urgency = models.CharField(
        choices=Urgency.choices,
        max_length=20,
        default=Urgency.MEDIUM,
    )

    status = models.CharField(
        choices=Status.choices,
        max_length=20,
        default=Status.BACKLOG
    )


# class TaskUserCommentMapping(models.Model):
#     created_at = models.DateField(default=now())
#     text = models.CharField(max_length=500)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     onTask = models.ForeignKey(Task, on_delete=models.CASCADE)


# class TaskUserIsAssignedMapping(models.Model):
#     created_at = models.DateField(default=now())
#     assignedUser = models.ForeignKey(User, on_delete=models.CASCADE)
#     onTask = models.ForeignKey(Task, on_delete=models.CASCADE)
