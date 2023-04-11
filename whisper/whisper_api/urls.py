from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.signin, name='signin'),
  path('logout/', views.signout, name='signout'),
  path('register/', views.register, name='register'),
  path('', views.home, name='home'),
  path('viewpost/<str:pk>/', views.singlePost, name='view-post'),
  path('profile/', views.profile, name='profile'),
  path('updatepost/<str:pk>/', views.editPost, name='edit-post'),
  path('deletepost/<str:pk>/', views.deletePost, name='delete-post'),
]
