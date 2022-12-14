from django.db import models
from dateutil import relativedelta
from enum import Enum

# MYStatus = Enum('Status', ['BACKLOG', 'TO_DO', 'IN_PROGRESS', 'REVIEW', 'DONE'])
# class Status(models.TextChoices):
#     BACKLOG = 'BL'
#     TO_DO = 'TD'


class Board(models.Model):
    title = models.CharField(max_length=100, default='')
    created_at = models.DateField(default=date.today())


class Task(models.Model):
    title = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=300, default='')
    # due_date = models.DateField(
    #     default=(datetime.today + relativedelta(months=+3))
    # )
    created_at = models.DateField(default=date.today())

    Status = models.TextChoices(
        'Status', ['BACKLOG', 'TO_DO', 'IN_PROGRESS', 'REVIEW', 'DONE']
    )

    status = models.CharField(
        choices=Status.choices,
        max_length=20,
        default=Status.BACKLOG
    )
