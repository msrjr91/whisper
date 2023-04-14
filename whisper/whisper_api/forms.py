from django.forms import ModelForm
from .models import Post, Profile

class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    exclude = ['user', 'commented']
    
    # widgets = {
    #   'content': form.TextInput
    # }

class UpdateProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['avatar']
