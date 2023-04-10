from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm


# Create your views here.
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
