from django.apps import AppConfig


class UsersTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_test'
    def ready(self):
        import users_test.signals