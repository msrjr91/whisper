from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Category, Comment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm

# Create your views here.
def signin(request):
  
  page = 'signin'
  
  if request.user.is_authenticated:
    return redirect('home')
    
  if request.method == 'POST':
    username = request.POST.get('username').lower()
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
      
  context = {'page': page}
  return render(request, 'signin.html', context)


def signout(request):
  logout(request)
  return redirect('home')


def register(request):
  page = 'register'
  form = UserCreationForm()
  
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'Registration failed')
    
  context = {'page': page, 
             'form': form,}
  return render(request, 'signin.html', context)


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
  comments = Comment.objects.filter(post_id=pk)
  context = {'post': post, 
             'comments': comments,}
  return render(request, 'post.html', context)


@login_required(login_url='/login')
def editPost(request, pk):
  post = Post.objects.get(id=pk)
  form = PostForm(instance=post)
  
  if request.user != post.user:
    return HttpResponse('You are not allowed to edit this post.')
  
  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      form.save()
      return redirect('home')
  context = {'form': form}
  return render(request, 'post_form.html', context)


@login_required(login_url='/login')
def deletePost(request, pk):
  post = Post.objects.get(id=pk)
  
  if request.user != post.user:
    return HttpResponse('You are not allowed to delete this post.')
  
  if request.method == 'POST':
    post.delete()
    return redirect('home')
  return render(request, 'delete.html')


def profile(request):
  return render(request, 'profile.html')
