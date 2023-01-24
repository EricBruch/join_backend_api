from .models import Task, TaskComment, TaskAssignedUser
from django.utils.timezone import now


def now_or_date(date):
    return now() if date is None else date


def create_and_get_Task(validated_data):
    task = Task.objects.create(
        title=validated_data.pop('title'),
        author=validated_data.pop('author'),
        category=validated_data.pop('category'),
        description=validated_data.pop('description'),
        due_date=validated_data.pop('due_date'),
        created_at=now_or_date(validated_data.pop('created_at')),
        board=validated_data.pop('board'),
        parent=validated_data.pop('parent'),
        urgency=validated_data.pop('urgency'),
        status=validated_data.pop('status')
    )
    task.save()
    return task


def create_task_comments(comments, task):
    for c in comments:
        newComment = TaskComment.objects.create(
            user=c.get('user'),
            task=task,
            text=c.get('text'),
            created_at=now_or_date(c.get('created_at'))
        )
        newComment.save()


def create_task_assigned_users(assignedUsers, task):
    for aU in assignedUsers:
        newAssignedUser = TaskAssignedUser.objects.create(
            user=aU.get('user'),
            task=task,
            created_at=now_or_date(aU.get('created_at'))
        )
        newAssignedUser.save()


def getMappedTaskInstance(instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.author = validated_data.pop('author', instance.author)
    instance.category = validated_data.pop('category', instance.category)
    instance.description = validated_data.pop(
        'description', instance.description
    )
    instance.due_date = validated_data.pop('due_date', instance.due_date)
    instance.created_at = validated_data.pop(
        'created_at', instance.created_at
    )
    instance.board = validated_data.pop('board', instance.board)
    instance.parent = validated_data.pop('parent', instance.parent)
    instance.urgency = validated_data.pop('urgency', instance.urgency)
    instance.status = validated_data.pop('status', instance.status)

    return instance
