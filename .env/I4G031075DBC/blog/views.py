from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    post_list = Post.objects.all()
    context = { "post_list": post_list }
    return render(request, "blog/index.html", context)

def PostListView(request):
    post_list = Post.objects.all()
    context = { "post_list": post_list }
    return render(request, "blog/post-list.html", context)

def PostCreateView(request):
    title = request.POST.get("title") 		
    body = request.POST.get("body") 

    if request.method == "POST":
        post = Post.objects.create(title=title, body=body)
        post.save()
    context = { }
    return render(request, "blog/post-form.html", context)



def PostDetailView(request):

    context = {}
    return render(request, "blog/post-detail.html", context)

def PostUpdateView(request):
    posts = Post.objects.all()
    context = { }
    return render(request, "blog/post-confirm-delete.html", context)

def PostDeleteView(request):
    posts = Post.objects.all()
    context = { "posts": posts }
    return render(request, "blog/post-confirm-delete.html", context)
