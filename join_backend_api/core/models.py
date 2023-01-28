from django.utils.timezone import now
from django.db import models
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model


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
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
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
    comments = models.ManyToManyField(
        User, through='TaskComment', related_name='taksOfUser')
    assignedUsers = models.ManyToManyField(
        User, through='TaskAssignedUser', related_name='tasksOfUser'
    )


class TaskComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=now())


class TaskAssignedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateField(default=now())
