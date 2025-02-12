from django.db import models

# Create your models here.
# If a new model field is added, must run 'makemigrations' to create
# a new migrations file, and 'migrate' to write changes to database
class About(models.Model):
    title = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title