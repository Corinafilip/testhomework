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
    categories = models.ManyToManyField(Category, related_name="tasks",
                                        help_text="Task categories")
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
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    task = models.ForeignKey('Task', on_delete=models.PROTECT)
    status = models.CharField(
        max_length=30,
        choices=STATUSES,
        default='NEW'
    )
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    title = models.CharField(max_length=100)






