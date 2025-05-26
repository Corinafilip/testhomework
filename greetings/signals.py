
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Task

@receiver(pre_save, sender=Task)
def notify_owner_on_status_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_task = Task.objects.get(pk=instance.pk)
    except Task.DoesNotExist:
        return

    if old_task.status != instance.status:
        # Только если статус изменился, отправляем email
        if instance.owner and instance.owner.email:
            send_mail(
                subject='Task Status Updated',
                message=f'Your task "{instance.title}" status changed from {old_task.status} to {instance.status}.',
                from_email='admin@example.com',
                recipient_list=[instance.owner.email],
            )