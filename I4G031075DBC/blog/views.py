from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    post_list = Post.objects.all()
    print("-----------------------")
    print(post_list)
    print("-----------------------")
    context = { "post_list": post_list }
    return render(request, "blog/post-list.html", context)

def PostListView(request):
    post_list = Post.objects.all()
    author = Post.objects.__getitem__("author")
    # FR_FIELD = DB.OBJECT.GET(DB_OBJ_HAVING_FR) 
    context['author'] = author

    print("-----------------------")
    print(post_list)
    print("-----------------------")
    context = { "post_list": post_list }
    
    return render(request, "blog/post-list.html", context)


def PostCreateView(request):
    print(request.POST)
    title = request.POST.get("title") 		
    body = request.POST.get("body")
    # writer = request.POST.get("writer")

    if request.method == "POST":
        post = Post.objects.create(title=title, body=body)
        print("-----------------------")
        print(post)
        print("-----------------------")
        post.save()
        return redirect('/')

    return render(request, "blog/post-form.html")



def PostDetailView(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post }
    return render(request, "blog/post-detail.html", context)

def PostUpdateView(request, pk):
    post = Post.objects.get(id=pk)
    post.update()
    context = {'post': post }
    return render(request, "blog/index.html", context)

def PostDeleteView(request, pk):
    post = Post.objects.get(id=pk)
    print("-----------------------")
    print(post)
    print("-----------------------")
    post.delete()

    return redirect('/')
