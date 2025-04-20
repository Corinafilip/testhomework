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





#Создайте эндпоинт для создания новой задачи.
# Задача должна быть создана с полями title, description, status, и deadline.

#Шаги для выполнения:

#Определите сериализатор для модели Task.

#Создайте представление для создания задачи.

#Создайте маршрут для обращения к представлению.#