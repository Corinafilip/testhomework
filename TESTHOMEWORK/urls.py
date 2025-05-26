"""
URL configuration for TESTHOMEWORK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from greetings.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from greetings.serializers.task_serializer import TaskCreateSerializer
from greetings.views import greetings
from greetings.views import create_task,  list_of_tasks, get_task_detail, new_tasks, in_progress_tasks, pending_tasks, blocked_tasks, done_tasks, overdue_tasks

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from greetings.views import RegisterView


schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your.email@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', greetings),
    path('task/create/', create_task),
    path('task/list_of_tasks/', list_of_tasks),
    path('task/get_task_detail/', get_task_detail),
    path('task/new_tasks/', new_tasks),
    path('task/in_progress_tasks/',in_progress_tasks),
    path('task/pending_tasks/', pending_tasks),
    path('task/blocked_tasks/',blocked_tasks),
    path('task/done_tasks/',done_tasks),
    path('tasks/overdue/', overdue_tasks),
    path('subtask', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtask/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update'),
    path('tasks/by-weekday/', TaskByWeekdayView.as_view(), name='tasks-by-weekday'),

    #path('subtasks/', SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/filter/', FilteredSubTaskListView.as_view(), name='filtered-subtask-list'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list-create'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('categories/<int:pk>/count_tasks/', CategoryViewSet.as_view({'get': 'count_tasks'}), name='category-count-tasks'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mytasks/', UserTasksListView.as_view(), name='user-tasks'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('register/', RegisterView.as_view(), name='register'),

]



