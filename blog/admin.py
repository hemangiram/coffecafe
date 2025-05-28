from django.contrib import admin
from .models import blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    
    
admin.site.register(blog)