from django.apps import AppConfig


class GreetingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greetings'

    def ready(self):
        import greetings.signals


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greetings'

    def ready(self):
        import greetings.signals


