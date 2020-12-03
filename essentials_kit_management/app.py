from django.apps import AppConfig


class EssentialsKitManagementAppConfig(AppConfig):
    name = "essentials_kit_management"

    def ready(self):
        from essentials_kit_management import signals # pylint: disable=unused-variable
