from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet, CommentsViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet, basename="boards")
router.register(r'tasks', TaskViewSet, basename="tasks")
router.register(r'comments', CommentsViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
