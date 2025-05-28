from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class blogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):  # Optional
    post = models.ForeignKey(blogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
