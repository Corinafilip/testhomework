from django.db import models



class Task(models.Model):
    STATUSES = [
        ('NEW', 'NEW'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('RESOLVED', 'RESOLVED')

    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=30,
        choices=STATUSES,
        default='NEW'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)


