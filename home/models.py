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


class Verification(models.Model):
    """
    Model created to render a view for the google verification.
    A characterfield is linked to store the google verification.
    """
    verification = models.CharField(max_length=250)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta created to order the Verification Model according
        to the updated_on field. It also determines the latest
        entry saved to the model.
        """
        ordering = ['updated_on']
        get_latest_by = ['updated_on']

    def __str__(self):
        return '%s' % (self.verification)
