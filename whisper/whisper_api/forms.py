from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Profile
from django.contrib.auth.models import User


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
      'content': forms.Textarea(attrs={'class': 'form-control  form-control-sm', 'placeholder': "Share your thoughts" }),
      'category': forms.Select(attrs={'class': 'form-select form-select-sm mb-3'}),
    }

class UpdateProfileForm(ModelForm):
  avatar = forms.ImageField(label="Profile Picture")
  
  class Meta:
    model = Profile
    fields = ('avatar', )

class RegisterUserForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
  first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
  last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
  
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
  def __init__(self, *args, **kwargs):
    super(RegisterUserForm, self).__init__(*args, **kwargs)
    
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'
