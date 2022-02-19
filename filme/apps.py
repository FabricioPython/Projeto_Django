from django.apps import AppConfig


# classe responsável por garantir a inclusão do app na parte de settings
class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
