from django.forms import ModelForm
from django import forms
from .models import Post, Profile

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    labels = {
      'content': "",
      'category': "Topic"
    }
    exclude = ['user', 'commented']
    
    widgets = {
      'content': forms.Textarea(attrs={'class': 'form-control  form-control-sm'}),
      'category': forms.Select(attrs={'class': 'form-select form-select-sm mb-3'}),
    }

class UpdateProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['avatar']
