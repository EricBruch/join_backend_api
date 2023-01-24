from .models import Board, Task, TaskComment, TaskAssignedUser
from .serializers import BoardSerializer, TaskSerializer, TaskCommentSerializer, TaskAssignedUserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class BoardViewSet(viewsets.ModelViewSet):
    '''
    This represents the boards that exists. Each kanban board is one board view.
    Multiple boards can exist and each board has its own taks
    '''
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TaskViewSet(viewsets.ModelViewSet):
    '''
    This shows all tasks that exists. 
    Each task belongs to a board, can have an arbitrary number of assigned users
    and tasks that belong to this task.
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CommentsViewSet(viewsets.ModelViewSet):
    '''
    This view shows all comments that exists for all tasks
    '''
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AssignedUsersViewSet(viewsets.ModelViewSet):
    '''
    This endpoint shows all assigned users that exist for all taks
    '''
    queryset = TaskAssignedUser.objects.all()
    serializer_class = TaskAssignedUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
