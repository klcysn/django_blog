from django.urls import path
from .views import HomePage, AboutPage, ContactPage, PostPage

urlpatterns = [
    path('', HomePage, name = "home"),
    path('about/', AboutPage, name = "about"),
    path('contact/', ContactPage, name = "contact"),
    path('post/', PostPage, name = "post"),
]