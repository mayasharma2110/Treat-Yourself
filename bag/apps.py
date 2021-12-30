from django.apps import AppConfig


class BagConfig(AppConfig):
    """ Create bag variable for use in session """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
