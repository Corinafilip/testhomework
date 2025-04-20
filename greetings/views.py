from django.core.serializers import serialize
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import status

from serializers.task_serializer import TaskCreateSerializer, TaskListSerializer, TaskDetailSerializer, TaskNewSerializer, TaskInProgressSerializer, TaskPendingSerializer, TaskBlockedSerializer, TaskDoneSerializer, TaskOverdueSerializer
from models import Task

from django.utils.timezone import now




def greetings(request):
    name = "Corina"
    return HttpResponse(f"<h1> Hello, {name}  </h1>")


@api_view(['POST'])
def create_task(request: Request):
    row_data = request.data
    serializer = TaskCreateSerializer(data=row_data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            data=serializer.data,
            status=201
        )
    else:
        return Response(
            data=serializer.errors,
            status=400
        )



@api_view(['GET',])
def list_of_tasks(request) -> Response:
   tasks = Task.objects.all()

   serializer = TaskListSerializer(tasks, many=True)
   return Response(
       data=serializer.data,
       status=200
   )

@api_view(['GET'])
def get_task_detail(request, task_id: int ) -> Response:
    try:
        task = Task.objects.get(id=task_id)
        serializer = TaskDetailSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response(
            data={"message": "Task not found"},
            status=404
        )



@api_view(['GET'])
def new_tasks(request):
    tasks = Task.objects.filter(status='NEW')
    serializer = TaskNewSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def in_progress_tasks(request):
    tasks = Task.objects.filter(status='IN PROGRESS')
    serializer = TaskInProgressSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pending_tasks(request):
    tasks = Task.objects.filter(status='PENDING')
    serializer = TaskPendingSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blocked_tasks(request):
    tasks = Task.objects.filter(status='BLOCKED')
    serializer = TaskBlockedSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def done_tasks(request):
    tasks = Task.objects.filter(status='DONE')
    serializer = TaskDoneSerializer(tasks, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def overdue_tasks(request):
    tasks = Task.objects.filter(deadline__isnull=False, deadline__lt=now())
    serializer = TaskOverdueSerializer(tasks, many=True)
    return Response(serializer.data)

