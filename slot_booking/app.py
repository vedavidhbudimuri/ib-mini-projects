from django.apps import AppConfig


class SlotBookingAppConfig(AppConfig):
    name = "slot_booking"

    def ready(self):
        from slot_booking import signals # pylint: disable=unused-variable
