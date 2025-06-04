from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Kahi custom permissions override ki to check karo
    # Example:
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.has_perm('main.view_customuser')
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.has_perm('main.change_customuser')
class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }
