from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('downloads/', views.download_list, name='download_list'),
  path('download video/<str:format>/', views.download_video, name='download_video'),
  path('download audio/<str:format>/', views.download_audio, name='download_audio'),
]