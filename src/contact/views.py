from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def ContactPage(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "We have received your email successfully")
            return redirect("contact")
    context = {
        "form" : form
    }
    
    return render(request, "contact.html", context)