from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()
    
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate = collaborate_form.save(commit=False)
            collaborate.read = False
            collaborate.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Messange is submitted and we will get back to you as soon as possible'
    )

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": CollaborateForm(),
        },
    )
