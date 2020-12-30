from django.urls import path
from .views import ContactPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ContactPage, name = "contact"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)