from django.core.serializers import serialize
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.decorators import api_view, action
from rest_framework import status, viewsets

from serializers.task_serializer import TaskCreateSerializer, TaskListSerializer, TaskDetailSerializer, TaskNewSerializer, TaskInProgressSerializer, TaskPendingSerializer, TaskBlockedSerializer, TaskDoneSerializer, TaskOverdueSerializer, SubTaskSerializer
from models import Task, SubTask

from django.utils.timezone import now
import calendar

from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from models import Category
from serializers.category_serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from permissions.owner_permission import IsOwner
from permissions.permissions import CanGetTasksPermission, CanGetSubTasksPermission
from rest_framework.permissions import IsAuthenticated


def greetings(request):
    name = "Corina"
    return HttpResponse(f"<h1> Hello, {name}  </h1>")


# ZADANIE 5

#class SubTaskListCreateView(APIView):
#    def get(self, request):
#        subtasks = SubTask.objects.all()
#        serializer = SubTaskSerializer(subtasks, many=True)
#        return Response(serializer.data)

#    def post(self, request):
#        serializer = SubTaskSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Zadanie 15-2
class SubTaskListCreateView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated, CanGetSubTasksPermission]
    #pagination_class = SubTaskPagination


    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class SubTaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    lookup_field = 'pk'

class SubTaskDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        try:
            subtask = SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return Response({'error': 'SubTask not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            subtask = SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return Response({'error': 'SubTask not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            subtask = SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return Response({'error': 'SubTask not found'},
                            status=status.HTTP_404_NOT_FOUND)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Zadanie 14
class TaskByWeekdayView(APIView):
    def get(self, request):
        weekday_param = request.query_params.get('day', None)

        if weekday_param:
            weekday_param = weekday_param.strip().capitalize()

            if weekday_param not in list(calendar.day_name):
                return Response(
                    {"error": "please write day names like Monday, Tuesday, etc."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Find tasks whose deadline falls on this weekday
            tasks = Task.objects.all()
            tasks = [task for task in tasks if task.deadline.strftime("%A") == weekday_param]
        else:
            tasks = Task.objects.all()

        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Zadanie 14 -2
class SubTaskPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5

# Vlad! Could you write me please if i need to make a new class SubTaskListView(APIView)
# or better add
# this piece of code to class  SubTaskListCreateView(APIView)?
# thank you in advance
class SubTaskListView(APIView):
    serializer_class = TaskListSerializer
    pagination_class = SubTaskPagination

    def get_queryset(self):
        return SubTask.objects.all().order_by('-created_at')



# Zadanie   14 -3
class FilteredSubTaskListView(ListAPIView):
    serializer_class = SubTaskSerializer
    pagination_class = SubTaskPagination

    def get_queryset(self):
        queryset = SubTask.objects.all().order_by('-created_at')

        task_title = self.request.query_params.get('task_title', None)
        subtask_status = self.request.query_params.get('status', None)

        if task_title:
            queryset = queryset.filter(task_title__icontains=task_title)

        if subtask_status:
            queryset = queryset.filter(status__iexact=subtask_status)

        return queryset



# zadanie 15 -1
class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    permission_classes = [IsAuthenticated, CanGetTasksPermission]


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    lookup_field = 'pk'

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





@api_view(['GET'])
def task_status_summary(request):
    status_counts = Task.objects.values('status').annotate(count=Count('id')).order_by('status')

    result = {status['status']: status['count'] for status in status_counts}

    return Response({
        'status_summary': result,
    })

# Zadanie 16 -3
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_destroy(self, instance):
        instance.delete()  # we use soft delete

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = category.task.count()
        return Response({'category': category.title, 'task_count': task_count})


# Zadanie 18
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs: Any):
        super().__init__(kwargs)
        self.action = None

    def get(self, request):
        return Response({"message": "Вы авторизованы"})

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        return [IsAuthenticated()]



