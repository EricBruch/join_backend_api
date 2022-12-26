from django.shortcuts import render

from .models import Board, Task, TaskCommentsMapping
from .serializers import BoardSerializer, TaskSerializer, TaskCommentSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'boards': reverse('board-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = TaskCommentsMapping.objects.all()
    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
