import os
import django
from django.utils import timezone
import datetime

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
    SubTask(title="Gather Information", description="Create presentation slides", status="NEW", deadline=timezone.now() + datetime.timedelta(days=1))
])