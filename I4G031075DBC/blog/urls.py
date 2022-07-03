from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("create/", views.PostCreateView, name="PostCreateView"),

    path("read/delete/<str:pk>", views.PostDeleteView, name="PostDeleteView"),
    path("delete/<str:pk>", views.PostDeleteView, name="PostDeleteView"),

    path("update/<str:pk>", views.PostUpdateView, name="PostUpdateView"),
    path("read/update/<str:pk>", views.PostUpdateView, name="PostUpdateView"),

    path("read/", views.PostListView, name="PostListView"),

    path("read/details/<str:id>", views.PostDetailView, name="PostDetailView"),
    path("details/<str:id>", views.PostDetailView, name="PostDetailView"),
]
