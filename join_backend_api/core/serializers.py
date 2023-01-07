from rest_framework import serializers
from .models import Board, Task, TaskComment, TaskAssignedUser
from accounts.models import CustomUser


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

    parent = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    comments = TaskCommentSerializer(
        source="taskcomment_set",  many=True,
    )

    assignedUsers = TaskAssignedUserSerializer(
        source="taskassigneduser_set", many=True,
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
        # title = validated_data.pop('title')
        # category = validated_data.pop('category')
        # description = validated_data.pop('description')
        # due_date = validated_data.pop('due_date')
        # created_at = validated_data.pop('created_at')
        # urgency = validated_data.pop('urgency')
        # status = validated_data.pop('status')

        # Task.objects.create(title=title, )

        orderedDicts = validated_data.pop('taskcomment_set')
        print('asdf', orderedDicts)

        for dict in orderedDicts:
            print(dict)
