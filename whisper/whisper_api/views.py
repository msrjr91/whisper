from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Comment, Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm, UpdateProfileForm, RegisterUserForm
from collections import defaultdict
from django.template.defaulttags import register

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
  form = RegisterUserForm()
  
  if request.method == 'POST':
    form = RegisterUserForm(request.POST)
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
  comments = Comment.objects.all()
  categories = Category.objects.all()
  all_users = User.objects.all()
  
  my_follows = None
  my_follows_ids = None
  if request.user.is_authenticated and request.user.profile.follows:
    my_follows = Profile.objects.get(id=request.user.id).follows.all()
    my_follows_ids = [x.id for x in my_follows]
    

    
  post_count = None
  comment_count = None
  if request.user.is_authenticated:
    post_count = len(Post.objects.filter(user_id=request.user.id))
    comment_count = len(Comment.objects.filter(user_id=request.user.id))
  
  form = PostForm()
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()
      return redirect('home')
    
  context = {'posts': posts, 
             'form': form,
             'categories': categories,
             'post_count': post_count,
             'comment_count': comment_count,
             'comments': comments,
             'my_follows': my_follows,
             'my_follows_ids': my_follows_ids,
             'all_users': all_users,
             }
  
  return render(request, 'home.html', context)


def singlePost(request, pk):
  post = Post.objects.get(id=pk)
  comments = Comment.objects.filter(post_id=pk).order_by('created')
  commented = post.commented.all()
  
  if request.method == 'POST':
    comment = Comment.objects.create(
      user = request.user,
      post = post,
      content = request.POST.get('comment-body'),
    )
    post.commented.add(request.user)
    return redirect('view-post', pk=post.id)
  
  context = {'post': post, 
             'comments': comments,
             'commented': commented}
  
  return render(request, 'post.html', context)

@login_required(login_url='/login')
def deleteComment(request, pk):
  comment = Comment.objects.get(id=pk)
  
  if request.user != comment.user:
    return HttpResponse('You are not allowed to delete this post.')
  
  if request.method == 'POST':
    comment.delete()
    return redirect('view-post', pk=comment.post_id)
  return render(request, 'delete.html')


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


def profile(request, pk):
  print("CURRENT USER: ",request.user.id)
  user = User.objects.get(id=pk)
  posts = user.post_set.all()
  comments = Comment.objects.all()
  all_comments = [comment.post.id for comment in comments]
  post_comment_count = frequencies(all_comments)  
  post_count = len(user.post_set.all())
  comment_count = len(user.comment_set.all())
  profile = Profile.objects.get(user_id=pk)

  if request.method == "POST":
    current_profile = request.user.profile
    action = request.POST['follow']
    if action == 'unfollow':
      current_profile.follows.remove(profile)
    elif action == 'follow':
      current_profile.follows.add(profile)
    current_profile.save()

  context = {'user': user,
             'posts': posts,
             'post_count': post_count,
             'comment_count': comment_count,
             'profile': profile,
             'post_comment_count': post_comment_count}
  return render(request, 'profile.html', context)

@login_required
def updateProfile(request, pk):
  user = User.objects.get(id=request.user.id)
  profile = Profile.objects.get(user__id=request.user.id)
  
  form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=profile)    
  if request.POST:
    form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=profile)    
    print("THE REQUEST:", request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  
  
  context = {'form': form,
             'profile': profile}
  return render(request, 'update_profile.html', context)


def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq) 


def searchUser(request):
  results = None
  if request.method == 'POST':
    searched = request.POST['user-search']
    results = User.objects.filter(username__contains=searched)
      
  context = {
             'searched': searched,
             'results': results,
             }
  return render(request, 'searchUser.html', context)
