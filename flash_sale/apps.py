from django.apps import AppConfig


class FlashSaleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flash_sale'

    def ready(self):
        import flash_sale.signals
