from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(default='New Post!',max_length=255)
    description = models.CharField(max_length=100, default='description should be here!')
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    loves = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="love")

    def __str__(self):
        return f'CodeShare by {self.author} created on {self.created_at}'
    
class Reply(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    loves = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="loves")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
