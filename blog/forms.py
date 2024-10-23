from django import forms

# Importing the Blog model from the current app's models
from .models import Blog  


# Define a form class for the Blog model
class BlogForm(forms.ModelForm):
    # Meta class to specify model-related options
    class Meta:
        # Specify the model this form is associated with
        model = Blog
        # Define which fields should be included in the form
        fields = ['title', 'content', 'image']
