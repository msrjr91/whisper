from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Post, Comment, Profile
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

# admin.site.register(Profile)
# Show profile info in user model
class UserProfile(admin.StackedInline):
  model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
  model = User
  # fields = ['__all__']
  inlines = [UserProfile]
  
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
