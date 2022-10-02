""" Blog App config file """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ Blog Config Settings """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
