from django.apps import AppConfig


class SetupsConfig(AppConfig):
    name = 'setups'

    def ready(self):
        from setups import signals
