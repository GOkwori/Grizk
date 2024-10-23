from django.apps import AppConfig

# Define configuration for the 'cart' application


class CartConfig(AppConfig):
    # Specify the default field type for automatically created primary keys
    default_auto_field = "django.db.models.BigAutoField"

    name = "cart"
