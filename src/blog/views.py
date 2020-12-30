from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib import messages 


def HomePage(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj" : page_obj
    }
    return render(request, "index.html", context)

def AboutPage(request):
    return render(request, "about.html")


def PostDetail(request, id):
    post = get_object_or_404(Post, id = id)
    print("my post", post)
    context = {
        "post" : post
    }
    return render(request, "post.html", context)

def AddPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have sent your message successfully ")
            return redirect("add-post")
    context = {
        "form" : form
    }
    return render(request, "add_post.html", context)
