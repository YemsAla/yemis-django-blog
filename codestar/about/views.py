from django.shortcuts import render
from .models import About
from .forms import CollaborateForm 

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
