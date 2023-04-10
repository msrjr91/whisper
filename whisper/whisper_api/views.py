from django.shortcuts import render, redirect
from .models import Post, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm

# Create your views here.
def signin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
  
    try: 
      user = User.objects.get(username=username)
    except:
      messages.error(request, f'No account with username {username} found. Please sign up.') 
    
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('home')
    else: 
      messages.error(request, f'Username: {username} or password is incorrect.') 
      
  context = {}
  return render(request, 'signin.html', context)

def signout(request):
  logout(request)
  return redirect('home')

def home(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  posts = Post.objects.filter(category__name__icontains=q)
  categories = Category.objects.all()
  form = PostForm()
  
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    
  context = {'posts': posts, 
             'form': form,
             'categories': categories,
             }
  
  return render(request, 'home.html', context)

def singlePost(request, pk):
  post = Post.objects.get(id=pk)
  context = {'post': post}
  return render(request, 'post.html', context)

def editPost(request, pk):
  post = Post.objects.get(id=pk)
  form = PostForm(instance=post)
  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form': form}
  return render(request, 'post_form.html', context)

def deletePost(request, pk):
  post = Post.objects.get(id=pk)
  if request.method == 'POST':
    post.delete()
    return redirect('home')
  return render(request, 'delete.html')

def profile(request):
  return render(request, 'profile.html')
