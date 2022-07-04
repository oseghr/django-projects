from django.shortcuts import redirect, render
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
    title = request.POST.get("title") 		
    body = request.POST.get("body")
    if title:
        post = Post.objects.create(title=title, body=body)
        post.save()
        return redirect(PostListView)
    return render(request, "blog/post-form.html")



def PostDetailView(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post }
    return render(request, "blog/post-detail.html", context)

def PostUpdateView(request, pk):
    post = Post.objects.get(id=pk)
    if post:
        title = request.POST.get("title") 		
        body = request.POST.get("body")
        post.update(title=title, body=body)
        return redirect(PostListView)
    context = {'post': post }
    return render(request, "blog/post-form.html", context)

def PostDeleteView(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')
