from rest_framework import serializers

from greetings.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    status = serializers.CharField(
        max_length=30,
        #choices=STATUSES,
        default='NEW'
    )
    deadline = serializers.DateField()

    class Meta:
        model = None
        fields = ('title', 'description', 'status', 'deadline')



class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'deadline')


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

#2: Эндпоинты для получения списка задач и конкретной задачи по её ID
#Создайте два новых эндпоинта для:

#Получения списка задач

#П#олучения конкретной задачи по её уникальному ID

#Шаги для выполнения:

#Создайте представления для получения списка задач и конкретной задачи.

#Создайте маршруты для обращения к представлениям.