from rest_framework import serializers
from .models import Board, Task, TaskComment, TaskAssignedUser


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title', 'created_at']


class TaskCommentSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    text = serializers.CharField()
    created_at = serializers.DateField()

    class Meta:
        model = TaskComment
        fields = ['user', 'task', 'created_at', 'text',]


class TaskAssignedUserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateField()

    class Meta:
        model = TaskAssignedUser
        fields = ['task', 'user', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')

    boardId = serializers.PrimaryKeyRelatedField(
        source="board", read_only=True
    )
    board_title = serializers.CharField(source='board.title', read_only=True)

    parent = serializers.PrimaryKeyRelatedField(read_only=True)

    comments = TaskCommentSerializer(
        source="taskcomment_set", read_only=True, many=True,
    )

    assignedUsers = TaskAssignedUserSerializer(
        source="taskassigneduser_set", read_only=True, many=True,
    )

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'author_name',
            'author_id',
            'category',
            'description',
            'due_date',
            'created_at',
            'boardId',
            'board_title',
            'parent',
            'urgency',
            'status',
            'comments',
            'assignedUsers'
        )
