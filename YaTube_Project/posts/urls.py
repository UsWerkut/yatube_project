from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.all_groups),
    path('group/<slug:slug>/', views.group_posts),
]