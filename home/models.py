"""
Xperiencedezignwiz home app URL Configuration

URLs for the home app setup according to home/views.py
home = the homepage
the social media views are setup to authorise login via the
various social media apps.
"""
from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    """
    Model created to render a view for the homepage.
    A foreignKey field is linked to store the username
    as the related_name 'home'
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='home',
        default='1'
    )

    def __str__(self):
        return '%s' % (self.username)


class Contact(models.Model):
    """
    Model created to render the contact page.
    A foreignKey field is linked to store the username
    as the related_name 'contact'
    """
    username = models.ForeignKey(
               User, on_delete=models.CASCADE, related_name='contact',
               default='1', blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta created to order the Contact Model according
        to the created on date.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'Contact request {self.body} by {self.name}'

    def __str__(self):
        return '%s' % (self.username)
