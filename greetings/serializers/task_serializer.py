from rest_framework import serializers

from greetings.models import Task
from sub_task_serializer import  SubTaskSerializer


class TaskCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    status = serializers.CharField(
        max_length=30,
        #choices=STATUSES,
        default='NEW'
    )
    deadline = serializers.DateField()

    our_sub_task_in_create = serializers.CharField(
        max_length=100,
        required=False

    )


    class Meta:
        model = None
        fields = ('title', 'description', 'status', 'deadline', 'our_sub_task')



class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'deadline')

# ZADANIE 3

class TaskDetailSerializer(serializers.ModelSerializer):
    our_sub_task = SubTaskSerializer()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    status = serializers.CharField()
    deadline = serializers.DateField()
    created_at = serializers.DateTimeField()
    resolved_at = serializers.DateTimeField()


    class Meta:
        model = Task
        fields = '__all__'



class TaskNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskInProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskBlockedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskOverdueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


