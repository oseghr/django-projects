from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("create/", views.PostCreateView, name="PostCreateView"),
    path("delete/", views.PostDeleteView, name="PostDeleteView"),
    path("update/", views.PostUpdateView, name="PostUpdateView"),
    path("read/", views.PostListView, name="PostListView"),
]
