from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from blog.models import blog, Post, Comment
from blog.forms import BlogPostForm
from django.http import HttpResponseForbidden
from blog.models import blogPost
from django.db.models import Q
from django.core.paginator import Paginator



def reservation(request):
    return render(request, 'reservation.html')

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        blog.objects.create(name=name, email=email, message=message)
        return render(request, 'index.html')
    return render(request, 'reservation.html')
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "User created successfully")
        return redirect('login')
    return render(request, 'register.html')


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            return redirect('list_post')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

@login_required
def role_redirect(request):
    user = request.user
    if user.is_superuser:
        print("welcome to admin")
        return redirect('admin:index')  # Django admin
    else:
        return redirect('home')  # Fallback to home page
        
   
 
    

def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def blogger_dashboard(request):
    return render(request, 'blogger_dashboard.html')







class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'





def index_redirect(request):
    return redirect('index.html')


@login_required(login_url='/login/')
def index_view(request):
    return render(request, 'login.html')  # Sirf template render karo, redirect mat karo

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')  # Ensure the template exists!

@login_required
def blogger_dashboard(request):
    return redirect('create_post') # Ensure the template exists!

@login_required
def create_post_blogger1(request):
    if getattr(request.user, 'role', None) != 'blogger':
        return HttpResponseForbidden("Aap Blogger1 nahi ho.")
    
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('list_post')
    return render(request, 'blogger.html', {'form': form})

@login_required
def create_post_blogger2(request):
    if getattr(request.user, 'role', None) != 'blogger2':
        return HttpResponseForbidden("Aap Blogger2 nahi ho.")
    
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('list_post')
    return render(request, 'blogger.html', {'form': form})

@login_required
def edit_post(request, post_id):
    if request.user.role != 'blogger':
        return HttpResponseForbidden("Sirf blogger post edit kar sakte hain.")
    post = get_object_or_404(Post, id=post_id)
    form = BlogPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('list_post')
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    if request.user.role != 'blogger':
        return HttpResponseForbidden("Sirf blogger post delete kar sakte hain.")
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('list_post')


@login_required
def list_post(request):
    blogger = request.user
    posts = Post.objects.filter(author=blogger) 
    posts_list = Post.objects.filter(author=blogger).order_by('-id')  # newest first
    paginator = Paginator(posts_list, 5)  # 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)   

    return render(request, 'list_post.html', {
        'posts': page_obj,  # pagination object
    })
        



@login_required
def blogger1_dashboard(request):
    return render(request, 'blog1.html')  # Blogger 1 ka custom page

@login_required
def blogger2_dashboard(request):
    return render(request, 'blog2.html')  # Blogger 2 ka custom page

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')


def home(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(name__icontains=query)  # Search by title (case-insensitive)
    else:
        posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, post_id):

        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all().order_by('-created_at')

        if request.method == 'POST':
            content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            messages.success(request, "Comment added successfully!")
            return redirect('post_detail', post_id=post_id)
        else:
            messages.error(request, "Comment cannot be empty.")

        return render(request, 'post_detail.html', {'post': post, 'comments': comments})

def create_post(request):
    return render(request, 'create_post.html')  
def view_drafts(request):
    drafts = Post.objects.filter(status='draft', author=request.user)
    return render(request, 'drafts.html', {'drafts': drafts})

def create_post(request):
     if not request.user.is_authenticated:
        return redirect('login')

     if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")  # ✅ Only here
    
            return redirect('home')
     else:
        form = BlogPostForm()
     return render(request, 'create_post.html', {'form': form})

   