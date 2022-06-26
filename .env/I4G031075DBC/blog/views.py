from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    context = { }
    return render(request, "blog/index.html", context)

def PostListView(request):
    post_list = Post.objects.all()
    context = { "post_list": post_list }
    return render(request, "blog/post-list.html", context)


def PostCreateView(request):
    print(request.POST)
    title = request.POST.get("title") 		
    body = request.POST.get("body")
    # author = request.POST.get("author")

    if request.method == "POST":
        post = Post.objects.create(title=title, body=body)
        print(post)
        post.save()

    return render(request, "blog/post-form.html")



def PostDetailView(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post }
    return render(request, "blog/post-detail.html", context)

def PostUpdateView(request):
    posts = Post.objects.update()
    context = { }
    return render(request, "blog/post-confirm-delete.html", context)

def PostDeleteView(request, id):
    posts = Post.objects.delete(id=id)
    context = { }
    return render(request, "blog/post-confirm-delete.html", context)
