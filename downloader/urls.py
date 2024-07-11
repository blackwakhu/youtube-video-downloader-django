from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('downloads/', views.download_list, name='download_list'),
]