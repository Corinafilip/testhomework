from django.contrib import admin
from .models import Task, SubTask #Category

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class TaskAdmin(admin.ModelAdmin):
    pass