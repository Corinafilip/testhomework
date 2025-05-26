from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CategoryManager(models.Manager):
    def get_queryset(self):
        # we filter for not delete
        return super().get_queryset().filter(is_deleted=False)


class Task(models.Model):
    STATUSES = [
        ('NEW', 'NEW'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('PENDING', 'PENDING'),
        ('BLOCKED', 'BLOCKED'),
        ('DONE', 'DONE'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    #categories = models.ManyToManyField('Category', related_name="tasks", help_text="Task categories")
    #subtask = models.ForeignKey(SubTask, on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(
        max_length=30,
        choices=STATUSES,
        default='NEW'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.title} is our task"

    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Our Task'
        unique_together = ('title', 'deadline')
        permissions = [
            ('can_get_tasks', 'Can get tasks'),
        ]



class SubTask(models.Model):
    STATUSES = [
        ('10%', '10%'),
        ('20%', '20%'),
        ('50%', '50%'),
        ('80%', '80%'),
        ('100%', '100%'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.PROTECT, related_name="subtasks")
    status = models.CharField(
        max_length=30,
        choices=STATUSES,
        default='NEW'
    )
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return f"{self.title} is our subtask"

    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
        unique_together = ('title', 'deadline')
        permissions = [
            ('can_get_subtasks', 'Can get subtasks'),
        ]




class Category(models.Model):
    title = models.CharField(max_length=100)
    task = models.ManyToManyField('Task', related_name="category", help_text="category")

# Zadanie 16 soft delete
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = CategoryManager()
    all_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_category'
        #ordering = ['-created_at']
        verbose_name = 'Task'
        #unique_together = ('title', 'task')






