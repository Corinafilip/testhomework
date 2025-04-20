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


#3 aggregate
#Создайте эндпоинт для получения статистики задач, таких как общее количество задач, количество задач по каждому статусу и количество просроченных задач.

#Шаги для выполнения:

#Определите представление для агрегирования данных о задачах.

#Создайте маршрут для обращения к представлению.

#Оформите ваш ответ следующим образом:

#Код эндпоинтов: Вставьте весь код представлений и маршрутов.

#Скриншоты ручного тестирования: Приложите скриншоты консоли или Postman, подтверждающие успешное выполнение запросов для каждого эндпои