from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
# If a new model field is added, must run 'makemigrations' to create
# a new migrations file, and 'migrate' to write changes to database
class About(models.Model):
    """
    Stores a single about me text.
    - need to include any models its ForeignKeys are related to
    - word User in the docstring refers to the model User in the auth app
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
