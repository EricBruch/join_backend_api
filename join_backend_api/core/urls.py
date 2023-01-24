from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TaskViewSet, CommentsViewSet, AssignedUsersViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet, basename="board")
router.register(r'tasks', TaskViewSet, basename="task")
router.register(r'comments', CommentsViewSet, basename='taskcomment')
router.register(r'assignedUsers', AssignedUsersViewSet, basename='taskassigneduser')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
