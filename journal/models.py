from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))  # constant

# Create your models here.
# If a new model field is added, must run 'makemigrations' to create
# a new migrations file, and 'migrate' to write changes to database
class Post(models.Model):
    """
    Stores a single blog post entry relatedto :model:"auth.User".
    - need to include any models its ForeignKeys are related to
    - word User in the docstring refers to the model User in the auth app
    """
    title = models.CharField(max_length=200, unique=True)  # must be unique
    slug = models.SlugField(max_length=200, unique=True)  # must be unique
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="journal_posts"
)
    # class allows superusers to upload media to a database model powered
    # by Cloudinary, ensures that image isn't stored in database,
    # but instead sent over to Cloudinary, saving just URL to database
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
