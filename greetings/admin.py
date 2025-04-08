from django.contrib import admin
from .models import Task, SubTask, Category  # Category

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'deadline')
    search_fields = ('title', 'deadline')
    list_filter = ('deadline',)
    ordering = ('-deadline',)
    fields = ('title', 'description', 'deadline')
    list_per_page = 5

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'deadline')
    search_fields = ('title', 'deadline')
    list_filter = ('status',)
    ordering = ('-status',)
    fields = ('title', 'description', 'status')
    list_per_page = 5

@admin.register(Category)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    list_filter = ('task',)
    fields = ('title', 'task', )
    list_per_page = 5