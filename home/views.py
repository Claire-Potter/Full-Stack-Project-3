"""
Xperiencedezignwiz home app views configuration

the index view is setup to display the homepage.
the social media views are setup to authorise login via the
various social media apps. This was completed as per the django
documentation:
https://django-rest-auth.readthedocs.io/en/latest/installation.html
"""

from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.views import View
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter)
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from .models import Home, User, Verification
from .forms import ContactForm


def index(request):
    """ A view to return the index page """
    queryset = Home.objects.all()
    home = get_object_or_404(queryset)

    context = {
        'home': home,
    }

    return render(request, 'index.html', context)


class FacebookLogin(SocialLoginView):
    """ A view to authorise login via Facebook """
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    """ A view to authorise login via Twitter """
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class Contact(View):
    """
    View created to render the Contact page.
    The view also references the Contact model
    and form in order to update the fields within
    the model tables
    """

    def get(self, request):
        """
        The get function retrieves the data
        to generate the step details page.

        self: The self is used to represent the instance of the class.
        request: The requests module allows you to send HTTP
        requests using Python.The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).
        Definition from https://www.w3schools.com/python/module_requests.asp

        If and else statement utilised to determine whether the user
        is logged in or not, if they are logged in, their name and email
        address will be derived from their user profile.
        """
        if User.objects.filter(username=self.request.user.username).exists():
            contact_form = ContactForm(initial={'name': request.user.username,
                                                'email': request.user.email})
        else:
            contact_form = ContactForm()
        return render(
            request,
            'contact.html',
            {
                'contact_form': contact_form,
            },
        )

    def post(self, request):
        """
        self: The self is used to represent the instance of the class.
        request: The requests module allows you to send HTTP
        requests using Python.The HTTP request returns a Response
        Object with all the response data (content, encoding, status, etc).
        Definition from https://www.w3schools.com/python/module_requests.asp

        If and else statement utilised to determine whether the user
        is logged in or not, if they are logged in, their name and email
        address will be derived from their user profile.
        """
        # create a variable to keep track of the form
        message_sent = False

        # check if form has been submitted
        if request.method == 'POST':
            # check if data from the form is clean
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.save()
                c_d = contact_form.cleaned_data
                subject = 'A new Request has been submitted'
                text_content = c_d['body']
                client_name = c_d['name']
                client_email = c_d['email']

                # send the email to the recipient
                email_message = EmailMultiAlternatives(from_email=settings
                                                       .DEFAULT_FROM_EMAIL,
                                                       to=['xperience'
                                                           'dezignwiz'
                                                           '@gmail.com'],
                                                       cc=['clairepotter'
                                                           '019@gmail.com'],
                                                       body=text_content,
                                                       subject=subject)
                email_message.template_id = ('d-9430602ecd'
                                             '0f411f8caa22367da72cbd')
                email_message.dynamic_template_data = {"body": text_content,
                                                       "body_two": client_name,
                                                       "body_three":
                                                       client_email,
                                                       "subject": subject}
                email_message.send(fail_silently=False)

                # set the variable initially created to True
                message_sent = True
            else:
                contact_form = ContactForm()

        return render(
            request,
            'contact.html',
            {
                'contact_form': contact_form,
                'message_sent': message_sent,

            },
        )


def verification(request):
    """ A view to return the google verification page """
    verification_id = (Verification.objects
                       .filter(verification="google50b8ec44e2d448c8.html")
                       .latest())

    context = {
        'verification_id': verification_id,
    }

    return render(request, 'google50b8ec44e2d448c8.html', context)
