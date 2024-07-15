from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('downloads/', views.download_list, name='download_list'),
  path('download/<str:video_id>/<str:sel_format>/', views.download_video, name='download_video'),
]