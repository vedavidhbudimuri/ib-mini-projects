from django.apps import AppConfig


class ProjectManagementPortalAppConfig(AppConfig):
    name = "project_management_portal"

    def ready(self):
        from project_management_portal import signals # pylint: disable=unused-variable
