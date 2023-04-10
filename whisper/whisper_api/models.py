from django.db import models
# Create your models here.


class User(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  is_active = models.BooleanField(default=False)
  # profilePicture = models.ImageField(default='', u
  date_joined = models.DateField(auto_now_add=True)
  # USERNAME_FIELD = 'username'
  # REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password', 'username']
  
  def __str__(self):
    return self.first_name


class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(max_length=255)
  category = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.content[0:50]

class Reply(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField(max_length=255)
  likes = models.IntegerField(default=0)
  dislikes = models.IntegerField(default=0)
  
  def __str__(self):
    return self.content[0:50]
