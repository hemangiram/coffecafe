
from django.contrib import admin
from django.urls import path
from . import views
from . views import *
from django.conf import settings  # <--- Add this
from django.conf.urls.static import static  #
from django.urls import path, include
from .views import role_redirect
from .views import list_post, role_redirect
from .views import create_post_blogger1, create_post_blogger2
app_name = 'blog' 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name='home'),
    path('reservation/',reservation, name='reserv'),
    path('save/',save, name='save'),
    path('login/' , user_login,name='login'),    
     path('logout' ,user_logout,name='logout'),    
    path('register' ,register,name='register'),   
    path('create/',create_post, name='create_post'),
    path('edit/<int:post_id>/',edit_post, name='edit_post'),
    path('delete/<int:post_id>/',delete_post, name='delete_post'),
    path('artical/<int:pk>/',PostDetailView.as_view(), name='post_details'),
      # Blog Post CRUD
    #path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('article/<int:pk>/', views.PostDetailView.as_view(), name='post_details'),
    path('role_redirect/', views.role_redirect, name='role_redirect'),
    # Dashboard View
    path('role_redirect/', role_redirect, name='role_redirect'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),  # <- Name it!
    path('blogger_dashboard/', blogger_dashboard, name='blogger_page'),
    #path('post/<int:pk>/', post_detail, name='post_detail'),  # post detail
    path('list/posts/', list_post, name='list_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('blog_one', blogger1_dashboard, name='blog1'),
    path('create/post/blogger1/', create_post_blogger1, name='blogger1'),
    path('create/post/blogger2/', create_post_blogger2, name='blogger2'),
    path('home', home, name='home'),  # homepage with all posts + search
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # detail
    path('create/', create_post, name='create_post'),
    path('post/new/', create_post, name='create_post'),
    path('drafts/', view_drafts, name='view_drafts')
  

 
    
    
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


