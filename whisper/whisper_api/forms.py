from django.forms import ModelForm
from django import forms
from .models import Post, Profile

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    exclude = ['user', 'commented']

class UpdateProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['avatar']
