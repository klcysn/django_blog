from django.urls import path
from .views import HomePage, AboutPage, ContactPage, PostDetail

urlpatterns = [
    path('', HomePage, name = "home"),
    path('about/', AboutPage, name = "about"),
    path('contact/', ContactPage, name = "contact"),
    path('<int:id>/post/', PostDetail, name = "post"),
]