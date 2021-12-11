"""
Xperiencedezignwiz home app views configuration

the index view is setup to display the homepage.
the social media views are setup to authorise login via the
various social media apps. This was completed as per the django
documentation:
https://django-rest-auth.readthedocs.io/en/latest/installation.html
"""

from django.shortcuts import render
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter)
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from .models import Home, Verification


def index(request):
    """ A view to return the index page """
    home = Home

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)


def verification(request):
    """ A view to return the google verification page """
    verification_id = (Verification.objects
                       .filter(verification="google50b8ec44e2d448c8.html")
                       .latest())

    context = {
        'verification_id': verification_id,
    }

    return render(request, 'google50b8ec44e2d448c8.html', context)


class FacebookLogin(SocialLoginView):
    """ A view to authorise login via Facebook """
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    """ A view to authorise login via Twitter """
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
