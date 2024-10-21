# Importing AppConfig from django.apps, which is used to configure application settings
from django.apps import AppConfig

# Define the configuration class for the 'blog' app
class BlogConfig(AppConfig):
    # Setting the default field type for auto-generated primary keys in models
    default_auto_field = "django.db.models.BigAutoField"
    
    # The name attribute defines the full Python path to the application
    name = "blog"
