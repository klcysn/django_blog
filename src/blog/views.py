from django.shortcuts import render, get_object_or_404
from .models import Post


def HomePage(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, "index.html", context)


def ContactPage(request):
    return render(request, "contact.html")

def AboutPage(request):
    return render(request, "about.html")


def PostDetail(request, id):
    post = get_object_or_404(Post, id = id)
    print("my post", post)
    context = {
        "post" : post
    }
    return render(request, "post.html", context)
