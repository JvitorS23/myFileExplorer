from django.apps import AppConfig


class ExplorerConfig(AppConfig):
    name = 'explorer'

    def ready(self):
        import explorer.signals # noqa