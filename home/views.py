"""
Xperiencedezignwiz home app views configuration

the index view is setup to display the homepage.
the social media views are setup to authorise login via the
various social media apps. This was completed as per the django
documentation:
https://django-rest-auth.readthedocs.io/en/latest/installation.html
"""

from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.views import  View
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter)
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from .models import Home, User
from .forms import EmailForm, ContactForm


def index(request):
    """ A view to return the index page """
    home = Home

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


def send_email(request):

    # create a variable to keep track of the form
    message_sent = False
    recipient_list = ""

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            c_d = form.cleaned_data
            subject = c_d['subject']
            text_content = c_d['message']
            recipient_list = c_d['recipients']

            # send the email to the recipent
            msg = EmailMultiAlternatives(from_email=settings
                                         .DEFAULT_FROM_EMAIL,
                                         reply_to=['xperience'
                                                   'dezignwiz@gmail.com'],
                                         to=['xperiencedezignwiz@gmail.com'],
                                         bcc=recipient_list, body=text_content,
                                         subject=subject)
            msg.template_id = "d-9430602ecd0f411f8caa22367da72cbd"
            msg.dynamic_template_data = {"body": text_content,
                                         "subject": subject}
            msg.send(fail_silently=False)

            # Unsubscribe groups
            # https://sendgrid.com/docs/ui/sending-email/unsubscribe-groups/
            msg.asm = {'group_id': 138000, 'groups_to_display': [
                       'XperienceDezignWiz']}

            # set the variable initially created to True
            message_sent = True

    else:
        form = EmailForm()

    return render(request, 'email.html', {

        'form': form,
        'message_sent': message_sent,
        'recipient_list': recipient_list,

    })


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
        contact_form = ContactForm()
        if User.objects.filter(username=self.request.user.username).exists():
            contact_form.instance.email = request.user.email
            contact_form.instance.name = request.user.username
        else:
            contact_form = CommentForm()


        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm(),
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
        if Contact.objects.filter(username=self.request.user.username).exists():
            contact_form = ContactForm(data=request.POST)
            contact_form.instance.email = request.user.email
            contact_form.instance.name = request.user.username
        else:
            contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.instance.email = request.user.email
            contact_form.instance.name = request.user.username
            body = body_form.save(commit=False)
            body.save()
            messages.success(request, 'Request submitted successfully')
        else:
            contac_form = ContactForm()

        progress_form = ProgressForm(data=request.POST)

        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm(),
            },
        )

