from django.apps import AppConfig


class ResourceManagementAppConfig(AppConfig):
    name = "resource_management"

    def ready(self):
        from resource_management import signals # pylint: disable=unused-variable
