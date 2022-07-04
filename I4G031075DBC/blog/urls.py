from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path("create/", views.PostCreateView, name="PostCreateView"),

    path("delete/<str:pk>", views.PostDeleteView, name="PostDeleteView"),

    path("update/<str:pk>", views.PostUpdateView, name="PostUpdateView"),

    path("read/", views.PostListView, name="PostListView"),

    path("details/<str:id>", views.PostDetailView, name="PostDetailView"),
]
