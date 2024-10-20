from django import forms
from .models import Blog  # Adjust this line based on your actual model

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']
