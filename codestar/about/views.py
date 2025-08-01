from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm 
from .models import CollaborateRequest

# Create your views here.
def about_page(request):
    """
    Display the about page content.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )

    
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    
    context = {
        'about': about,
        'collaborate_form': collaborate_form,
    }
    
    # return render(
    #     request,
    #     "about/about.html",
    #     {"about": about},
    # )
    return render(
    request,
    "about/about.html",
    {
        'about': about,
        'collaborate_form': collaborate_form,
    },
)
