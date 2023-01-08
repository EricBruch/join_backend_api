from rest_framework import serializers
from .models import Board, Task, TaskComment, TaskAssignedUser
from accounts.models import CustomUser
from django.utils.timezone import now


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title', 'created_at']


class TaskCommentSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all())
    text = serializers.CharField()
    created_at = serializers.DateField(required=False)

    class Meta:
        model = TaskComment
        fields = ['user', 'task', 'created_at', 'text',]


class TaskAssignedUserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all())
    created_at = serializers.DateField(required=False)

    class Meta:
        model = TaskAssignedUser
        fields = ['task', 'user', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all())

    created_at = serializers.DateField(required=False)

    board_id = serializers.PrimaryKeyRelatedField(
        source="board", queryset=Board.objects.all()
    )
    board_title = serializers.CharField(source='board.title', read_only=True)

    parent = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), allow_null=True)

    comments = TaskCommentSerializer(
        source="taskcomment_set",
        many=True,
        default=[]
    )

    assignedUsers = TaskAssignedUserSerializer(
        source="taskassigneduser_set",
        many=True,
        default=[]
    )

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'author',
            'author_name',
            'category',
            'description',
            'due_date',
            'created_at',
            'board_id',
            'board_title',
            'parent',
            'urgency',
            'status',
            'comments',
            'assignedUsers'
        )

    def create(self, validated_data):
        task = create_and_get_Task(validated_data)

        comments = validated_data.pop('taskcomment_set')
        if comments:
            create_task_comments(comments, task)

        assignedUsers = validated_data.pop('taskassigneduser_set')
        if assignedUsers:
            create_task_assigned_users(assignedUsers, task)

        return task

    def update(self, instance, validated_data):
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

        instance.save()
        return instance


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


def now_or_date(date):
    return now() if date is None else date
