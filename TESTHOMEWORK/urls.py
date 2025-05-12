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
from django.urls import path
from greetings.views import *


from greetings.serializers.task_serializer import TaskCreateSerializer
from greetings.views import greetings
from greetings.views import create_task,  list_of_tasks, get_task_detail, new_tasks, in_progress_tasks, pending_tasks, blocked_tasks, done_tasks, overdue_tasks


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
    path('subtasks/', SubTaskListView.as_view(), name='subtask-list'),



]
