from django.db import models

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
    categories = models.ManyToManyField('Category', related_name="tasks", help_text="Task categories")
    status = models.CharField(
        max_length=30,
        choices=STATUSES,
        default='NEW'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title


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
    status = models.CharField(
        max_length=30,
        choices=STATUSES,
        default='NEW'
    )
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    task = models.ManyToManyField('Task', related_name="category", help_text="category")
    def __str__(self):
        return self.title






