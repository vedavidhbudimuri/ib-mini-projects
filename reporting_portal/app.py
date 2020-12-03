from django.apps import AppConfig


class ReportingPortalAppConfig(AppConfig):
    name = "reporting_portal"

    def ready(self):
        from reporting_portal import signals # pylint: disable=unused-variable
