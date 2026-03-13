from django.apps import AppConfig

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prj.app'
    label = 'app' # Tento řádek přidáváme pro jistotu, aby Django vědělo, jak tabulky pojmenovat