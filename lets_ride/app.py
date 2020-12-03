from django.apps import AppConfig


class LetsRideAppConfig(AppConfig):
    name = "lets_ride"

    def ready(self):
        from lets_ride import signals # pylint: disable=unused-variable
