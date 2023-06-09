from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Category(models.Model):
  name = models.CharField(max_length=100)
  
  class Meta:
    ordering = ['-name']
  
  def __str__(self):
    return self.name

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(max_length=255)
  commented = models.ManyToManyField(User, related_name='commenters', blank=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
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
  
  class Meta:
    ordering = ['-updated', '-created']
  
  def __str__(self):
    return self.content[0:50]

    
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  follows = models.ManyToManyField("self",
                                   related_name='followed_by',
                                   symmetrical=False,
                                   blank=True)
  avatar = models.ImageField(null=True, max_length=300, default="/whisper/static/images/a-profile.jpg", upload_to='whisper/Whisper/static/images')
  
  
  def __str__(self):
    return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    user_profile = Profile(user=instance)
    user_profile.save()
    user_profile.follows.set([instance.profile.id, 1])
    user_profile.save()
    print('PROFILE CREATED!', instance)
    
# post_save.connect(create_profile, sender=User)

# class Avatar(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)

#   def __str__(self):
#     return self.user
