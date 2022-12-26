from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet, basename="boards")
router.register(r'tasks', TaskViewSet, basename="tasks")

urlpatterns = [
    path('', include(router.urls)),
]
