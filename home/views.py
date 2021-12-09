from django.shortcuts import render
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter)
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import Home


def index(request):
    """ A view to return the index page """
    # Display and filter blog posts on index page
    home = Home

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    # callback_url = CALLBACK_URL_YOU_SET_ON_GITHUB
    client_class = OAuth2Client
