from django.db import models
import datetime
from dateutil.relativedelta import *

# MYStatus = Enum('Status', ['BACKLOG', 'TO_DO', 'IN_PROGRESS', 'REVIEW', 'DONE'])
# class Status(models.TextChoices):
#     BACKLOG = 'BL'
#     TO_DO = 'TD'


class Board(models.Model):
    title = models.CharField(max_length=100, default='')
    created_at = models.DateField(default=datetime.datetime.now())


class Task(models.Model):
    title = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=300, default='')
    due_date = models.DateField(
        default=(datetime.datetime.now() + relativedelta(months=+3))
    )
    created_at = models.DateField(default=datetime.datetime.now())
    board = models.ForeignKey('Board', on_delete=models.CASCADE)

    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE
    )
    # subtask = models.ManyToManyField('self', blank=True)

    Urgency = models.TextChoices('Urgency', ['URGENT', 'MEDIUM', 'LOW'])
    urgency = models.CharField(
        choices=Urgency.choices,
        max_length=20,
        default=Urgency.MEDIUM,
    )

    Status = models.TextChoices(
        'Status', ['BACKLOG', 'TO_DO', 'IN_PROGRESS', 'REVIEW', 'DONE']
    )
    status = models.CharField(
        choices=Status.choices,
        max_length=20,
        default=Status.BACKLOG
    )
