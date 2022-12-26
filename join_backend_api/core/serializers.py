from rest_framework import serializers
from .models import Board, Task


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title', 'created_at']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')

    boardId = serializers.PrimaryKeyRelatedField(
        source="board", read_only=True
    )
    board_title = serializers.CharField(source='board.title', read_only=True)

    parent = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
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
            # 'comments',
            # 'assignedUsers'
        ]

# TaskSerializer._declared_fields['parent'] = TaskSerializer()
