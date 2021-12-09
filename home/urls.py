from django.urls import path
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rest-auth/facebook/',
         views.FacebookLogin.as_view(),
         name='fb_login'),
    path('rest-auth/twitter/',
         views.TwitterLogin.as_view(),
         name='twitter_login'),
    path('rest-auth/github/',
         views.GitHubLogin.as_view(),
         name='github_login'),
    path('socialaccounts/',
         SocialAccountListView.as_view(),
         name='social_account_list'),
    path('socialaccounts/(P<pk>\d+)/disconnect/',
         SocialAccountDisconnectView.as_view(),
         name='social_account_disconnect'),
]
