from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))  # constant

# Create your models here.
# If a new model field is added, must run 'makemigrations' to create
# a new migrations file, and 'migrate' to write changes to database
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # must be unique
    slug = models.SlugField(max_length=200, unique=True)  # must be unique
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="journal_posts"
)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
