from django.db import models
from django.utils.text import slugify

# Define the Blog model to store blog posts


class Blog(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)

    # Slug for the blog post (used in URLs, auto-generated if blank)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    # Main content of the blog post
    content = models.TextField()

    # Reference to the user who authored the blog post (foreign key to the User model)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Optional image associated with the blog post
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    # Timestamp when the blog post was created (auto-generated)
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp when the blog post was last updated (auto-updated)
    updated_at = models.DateTimeField(auto_now=True)

    # Boolean field to indicate if the blog post is published
    published = models.BooleanField(default=False)

    # Override the save method to auto-generate a unique slug if not provided
    def save(self, *args, **kwargs):
        # If the slug is not set, generate one
        if not self.slug:
            self.slug = self.generate_unique_slug()
        # Call the superclass save method to save the object
        super().save(*args, **kwargs)

    # Generate a unique slug for the blog post title
    def generate_unique_slug(self):
        # Create a slug from the title using Django's slugify utility
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        # Check if the slug already exists, and if so, append a number to make it unique
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1

        # Return the unique slug
        return unique_slug

    # String representation of the Blog object, returns the blog title
    def __str__(self):
        return self.title
