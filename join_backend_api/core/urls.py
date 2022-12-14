from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet, CommentsViewSet, AssignedUsersViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet, basename="boards")
router.register(r'tasks', TaskViewSet, basename="tasks")
router.register(r'comments', CommentsViewSet, basename='comments')
router.register(r'assignedUsers', AssignedUsersViewSet, basename='assignedUsers')

urlpatterns = [
    path('', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
