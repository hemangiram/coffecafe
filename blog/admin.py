from django.contrib import admin
from .models import blog, blogPost, Comment



class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('email',)

# Customize blogPost model in admin
@admin.register(blogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
# Customize Comment model in admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'created_at')
    search_fields = ('post__title', 'author__username', 'body')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'
    
    
class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)  # Custom CSS ka path
        }
        admin.site.register(blog)
