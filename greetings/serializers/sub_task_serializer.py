from rest_framework import serializers

from greetings.models import SubTask


# (title, description, task, status, deadline, created_at(not necessary))
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

class SubTaskCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    deadline = serializers.DateField()
    created_at = serializers.DateField(
        read_only=True,
    )

    class Meta:
        model = None
        fields = ('title', 'description','deadline', 'created_at')