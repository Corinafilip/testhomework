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


from greetings.serializers.task_serializer import TaskCreateSerializer
from greetings.views import greetings
from greetings.views import create_task,  list_of_tasks, get_task_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', greetings),
    path('task/create/', create_task),
    path('task/create/', list_of_tasks),
    path('task/create/', get_task_detail),

]
