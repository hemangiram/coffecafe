from django.http import HttpResponse
from django.shortcuts import render
from blog.models import blog 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from blog.models import blogPost
from .forms import BlogPostForm

    # return HttpResponse("Hello, world. You're at the blog index.")
def reservation(request):
    return render(request, 'reservation.html')
    # return HttpResponse("Hello, world. You're at the blog index.")
def save(request):
    print("hello")
    en=''
    if request.method == 'POST':
        print("hello")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        

        print("hello")
        
        # Save the data to the database or perform any other action
        # For example, you can print the data to the console
        blog.objects.create(name=name, email=email, message=message)
        return render(request, 'index.html')
    else:
        return render(request, 'reservation.html')
#     # return HttpResponse("Hello, world. You're at the blog index.")

def user_login(request):
    if request.method=="POST":
        print("hello")
        print("POST:::")
        print(request.POST)
        username_form=request.POST.get('username')
        password_form=request.POST.get('password')

        print("username_form:", username_form)
        print("password_form:", password_form) 

        user= authenticate(username=username_form,password=password_form)
        print('user:', user)  
        print(username_form)
        if user is not None:
            print("asdsad vjhj")
            login(request,user)
            print("56565656545")
            return render(request, 'index.html') # Redirect to the index view after successful login
        else:
            messages.error(request,"invalid credentials")
            print("asdsad")
    return render(request, 'login.html')
    # return HttpResponse("Hello, world. You're at the blog index.")    


def register(request):
    if request.method=="POST":
        print("hello")
        username=request.POST.get('username')
        password=request.POST.get('password')
        print("username:", username)
        print("password:", password)
        if User.objects.filter(username=username).exists():
            print("hello")
            messages.error(request,"username already exists")
            return redirect("login") 
        else:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            print("user created")
            messages.success(request,"user created successfully")
            return redirect("login") 
    return render(request, 'register.html')
    # return HttpResponse("Hello, world. You're at the blog index.")
def user_logout(request):
            logout(request)
            return redirect("login")


@login_required(login_url='/login/')  # Redirect to login page if not logged in
def index_view(request):
        print("hello")
        return redirect('login')
      

def index_redirect(request):
    return redirect('index.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')

            return redirect('list_posts')
    else:
        form = BlogPostForm()
        messages.info(request, 'Please fill out the form to create a new post.')    
    return render(request, 'create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(blogPost, pk=post_id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('list_posts')
    else:
        form = BlogPostForm(instance=post)
    messages.info(request, 'You are editing a post.')
    return render(request, 'edit_post.html', {'form': form})

def list_posts(request):
    posts = blogPost.objects.all().order_by('-created_at')
    if not posts:
        messages.info(request, 'No posts available.')
    else:
        messages.success(request, f'{posts.count()} posts found.')
    return render(request, 'list_posts.html', {'posts': posts})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(blogPost, id=post_id)
    if request.user != post.author:
        messages.error(request, 'You are not authorized to delete this post.')
    else:
        post.delete()
        messages.success(request, 'Post deleted successfully.')
    return redirect('home')
