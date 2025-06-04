from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings 



# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES =(
        ('admin','Admin'),
        ('blogger','Blogger'),
        ('user','User'),
        
        
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='main_posts'  # <--- ADD THIS LINE
    )
    # ... your other fieldsclass Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='main_posts'  # Add this to avoid clashes if you have another Post model in a different app
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title