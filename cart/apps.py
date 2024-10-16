from django.apps import AppConfig

# Define configuration for the 'cart' application


class CartConfig(AppConfig):
    # Specify the default field type for automatically created primary keys in models
    default_auto_field = "django.db.models.BigAutoField"

    # Set the name of the application; this should match the directory name of the app
    name = "cart"
