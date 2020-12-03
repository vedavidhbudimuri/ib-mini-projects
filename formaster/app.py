from django.apps import AppConfig


class FormasterAppConfig(AppConfig):
    name = "formaster"

    def ready(self):
        from formaster import signals # pylint: disable=unused-variable
