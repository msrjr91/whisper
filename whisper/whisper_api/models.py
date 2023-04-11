from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(max_length=255)
  commented = models.ManyToManyField(User, related_name='commenters', blank=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ['-updated', '-created']
  
  def __str__(self):
    return self.content[0:50]

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField(max_length=255)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.content[0:50]
