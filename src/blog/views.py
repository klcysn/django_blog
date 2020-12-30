from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


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
