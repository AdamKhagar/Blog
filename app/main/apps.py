from django.apps import AppConfig


class MainConfig(AppConfig):
    default_site = 'config.admin.MyAdminSite'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


