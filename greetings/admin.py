from django.contrib import admin
from django.db.models import QuerySet
from .models import Task, SubTask, Category  # Category

class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTaskInline]
    list_display = ('title', 'description', 'deadline')
    search_fields = ('title', 'deadline')
    list_filter = ('deadline',)
    ordering = ('-deadline',)
    fields = ('title', 'description', 'deadline')
    list_per_page = 5

    def short_title(self, obj: Task) -> str:
        return f"{obj.title[:10]} "




@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    actions = ['set_subtask_status_done',]
    list_display = ('task__title', 'title', 'description', 'deadline', 'status')

    def set_subtask_status_done(self, request, objs: QuerySet)  -> None:
        for obj in objs:
            obj.status = 'DONE'
            obj.save()
        self.message_user(request, f"Status is updated for {objs.count()}.")
    set_subtask_status_done.short_description = "Set SubTask Status"

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

