from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('login/', views.signin, name='signin'),
  path('logout/', views.signout, name='signout'),
  path('register/', views.register, name='register'),
  path('', views.home, name='home'),
  path('viewpost/<str:pk>/', views.singlePost, name='view-post'),
  path('profile/<str:pk>/', views.profile, name='profile'),
  path('updatepost/<str:pk>/', views.editPost, name='edit-post'),
  path('deletepost/<str:pk>/', views.deletePost, name='delete-post'),
  path('deletecomment/<str:pk>/', views.deleteComment, name='delete-comment'),
  path('updateprofile/<str:pk>/', views.updateProfile, name='update-profile'),
  path('searchuser/', views.searchUser, name='search-user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
