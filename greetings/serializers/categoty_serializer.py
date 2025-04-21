from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from greetings.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ('title', 'task')

    def create(self, validated_data: dict[str]) -> Category:
        title = validated_data.get('title')
        if Category.objects.filter(title=title).exists():
            raise ValidationError({'title': 'this title exists'})
        return super().create(**validated_data)

    def update(self, instance: Category, validated_data: dict[str]) -> Category:
        title = validated_data.get('title')
        if title in Category.objects.exclude(id=instance.id).filter(title=title).exists():
            raise ValidationError({'title': 'this title exists'})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return super().update(instance, validated_data)

