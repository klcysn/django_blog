from django.shortcuts import render
from .models import Post


def HomePage(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, "index.html", context)

def PostPage(request):
    return render(request, "post.html")


def ContactPage(request):
    return render(request, "contact.html")

def AboutPage(request):
    return render(request, "about.html")
# Create your views here.
