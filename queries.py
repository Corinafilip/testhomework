import os
import django
from django.utils import timezone
import datetime
from django.db.models import Q

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_config.settings')
django.setup()


from greetings.models import  Task, SubTask, Category


we_create_new_task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="NEW",
    deadline=timezone.now() + datetime.timedelta(days=3)
)

we_create_bulk_subtask = SubTask.objects.bulk_create([

    SubTask(title="Gather Information", description="Find necessary info for the presentation", status="NEW", deadline=timezone.now() + datetime.timedelta(days=2)),
    SubTask(title="Create Slides", description="Create presentation slides", status="NEW", deadline=timezone.now() + datetime.timedelta(days=1))
])

#select

select_new_tasks = Task.objects.filter(status="NEW")

select_subtask_done_but_expired = SubTask.objects.filter(
    Q(status="DONE") & Q(deadline__lt=timezone.now())

)

#change

Task.objects.filter(title="Prepare presentation").update(status="IN PROGRESS")

SubTask.objects.filter(title="Gather Information").update(deadline=timezone.now() - datetime.timedelta(days=2))

SubTask.objects.filter(title="Create Slides").update(title="Create and format presentation slides")

#delete

delete_task_prepare_presentation = Task.objects.get(title="Prepare presentation")
delete_task_prepare_presentation.delete()

#delete subtask
delete_subtask1 = SubTask.objects.get(title="Gather Information")
delete_subtask2 = SubTask.objects.get(title="Create and format presentation slides")

delete_subtask1.delete()
delete_subtask2.delete()