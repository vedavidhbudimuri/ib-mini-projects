from django.apps import AppConfig


class CovidDashboardAppConfig(AppConfig):
    name = "covid_dashboard"

    def ready(self):
        from covid_dashboard import signals # pylint: disable=unused-variable
