from django import forms
from blog.models import blogPost  # assuming the model is in blog/models.py
from django import forms
from blog.models import blogPost,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogPostForm(forms.ModelForm):  # <-- Correct name and capitalization
    class Meta:
        model = blogPost
        fields = ['title', 'content']
       
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']