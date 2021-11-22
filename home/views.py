from django.shortcuts import render
from .models import Home


def index(request):
    """ A view to return the index page """
    # Display and filter blog posts on index page
    home = Home

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)
