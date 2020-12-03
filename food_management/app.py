from django.apps import AppConfig


class FoodManagementAppConfig(AppConfig):
    name = "food_management"

    def ready(self):
        from food_management import signals # pylint: disable=unused-variable
