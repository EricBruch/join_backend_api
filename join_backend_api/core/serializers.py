from rest_framework import serializers
from .models import Board, Task, TaskComment, TaskAssignedUser
from accounts.models import CustomUser
from django.utils.timezone import now
from .utils import (
    create_and_get_Task,
    create_task_comments,
    create_assigned_users,
    getMappedTaskInstance,
)


class BoardSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(required=False, default=now().date)

    class Meta:
        model = Board
        fields = ["id", "title", "created_at"]


class TaskCommentSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    text = serializers.CharField()
    created_at = serializers.DateField(required=False)

    class Meta:
        model = TaskComment

        fields = [
            "user",
            "task",
            "created_at",
            "text",
        ]


class TaskAssignedUserSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    created_at = serializers.DateField(required=False)

    class Meta:
        model = TaskAssignedUser
        fields = ["task", "user", "created_at"]


class TaskSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    created_at = serializers.DateField(required=False)

    board_id = serializers.PrimaryKeyRelatedField(
        source="board", queryset=Board.objects.all()
    )
    board_title = serializers.CharField(source="board.title", read_only=True)

    parent = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), allow_null=True
    )

    comments = TaskCommentSerializer(source="taskcomment_set", many=True, default=[])

    assignedUsers = TaskAssignedUserSerializer(
        source="taskassigneduser_set", many=True, default=[]
    )

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "author",
            "author_name",
            "category",
            "description",
            "due_date",
            "created_at",
            "board_id",
            "board_title",
            "parent",
            "urgency",
            "status",
            "comments",
            "assignedUsers",
        )

    def create(self, validated_data):
        task = create_and_get_Task(validated_data)

        comments = validated_data.pop("taskcomment_set")
        if comments:
            create_task_comments(comments, task)

        assignedUsers = validated_data.pop("taskassigneduser_set")
        if assignedUsers:
            create_assigned_users(assignedUsers, task)

        return task

    def update(self, instance, validated_data):
        mappedInstance = getMappedTaskInstance(instance, validated_data)
        mappedInstance.save()
        return mappedInstance
