"""
Xperiencedezignwiz home app model Configuration

Home model created to render a view for the homepage.
It stores the home page image and title.
Contact model created to render the contact page
and to store all contact requests submitted by users.
Admin can access this via the admin pane.
Verification model created to render a view for
the google verification and store the verification
code - which is not a secret field.

"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Home(models.Model):
    """
    Model created to render a view for the homepage.
    A foreignKey field is linked to store the username
    as the related_name 'home'. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    name = models.CharField(max_length=80)
    home_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    do_not_delete = models.BooleanField(default=True)

    class Meta:
        """
        Meta created to order the Contact Model according
        to the created on date.
        """
        ordering = ['-created_on']
        verbose_name_plural = "Home"

    def __str__(self):
        return '%s' % (self.name)


class Contact(models.Model):
    """
    Model created to render the contact page.
    A foreignKey field is linked to store the username
    as the related_name 'contact'. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    username = models.ForeignKey(
               User, on_delete=models.CASCADE, related_name='contact',
               default='1', blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    do_not_delete = models.BooleanField(default=False)

    class Meta:
        """
        Meta created to order the Contact Model according
        to the created on date.
        """
        ordering = ['-created_on']
        verbose_name_plural = "Contact Requests"

    def __str__(self):
        return f'Contact request {self.body} by {self.name}'


class Verification(models.Model):
    """
    Model created to render a view for the google verification.
    A characterfield is linked to store the google verification.
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    verification = models.CharField(max_length=250)
    updated_on = models.DateTimeField(auto_now_add=True)
    do_not_delete = models.BooleanField(default=True)

    class Meta:
        """
        Meta created to order the Verification Model according
        to the updated_on field. It also determines the latest
        entry saved to the model.
        """
        ordering = ['updated_on']
        get_latest_by = ['updated_on']
        verbose_name_plural = "Verification Id"

    def __str__(self):
        return '%s' % (self.verification)
