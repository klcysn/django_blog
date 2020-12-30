from django.urls import path
from .views import HomePage, AboutPage, PostDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage, name = "home"),
    path('about/', AboutPage, name = "about"),
    path('<int:id>/post/', PostDetail, name = "post"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)