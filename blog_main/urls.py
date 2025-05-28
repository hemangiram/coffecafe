
from django.contrib import admin
from django.urls import path
from . import views
from . views import *
from django.conf import settings  # <--- Add this
from django.conf.urls.static import static  #

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='home'),
    path('reservation/',reservation, name='reserv'),
    path('save/',save, name='save'),
    path('login/' ,user_login,name='login'),    
     path('logout' ,user_logout,name='logout'),    
    path('register' ,register,name='register'),   
    path('',list_posts, name='list_posts'),
    path('create/',create_post, name='create_post'),
    path('edit/<int:post_id>/',edit_post, name='edit_post'),
    path('delete/<int:post_id>/',delete_post, name='delete_post'),
 
    
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)