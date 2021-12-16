from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Survey(models.Model):
    """A survey created by a user."""

    title = models.CharField(max_length=64)
    survey_image = CloudinaryField('image', default='placeholder', blank=True,
                                   null=True)
    is_active = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Gender(models.Model):
    """
    Model created to store the gender choices.
    """
    title = models.CharField(max_length=80)
    order_number = models.IntegerField()

    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


class AgeRange(models.Model):
    """
    Model created to store the age_range choices.
    """
    title = models.CharField(max_length=80)
    order_number = models.IntegerField()

    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


class Industry(models.Model):
    """
    Model created to store the Industry choices.
    """
    title = models.CharField(max_length=250)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return '%s' % (self.title)


class DefaultQuestion(models.Model):
    """Add default questions to a survey"""

    survey = models.ForeignKey(Survey,
                               on_delete=models.CASCADE,
                               related_name="defaultquestions_set")
    name = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE,
                               related_name="gender_set")
    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE,
                                  related_name="age_range_set")

    industry = models.ForeignKey(Industry, on_delete=models.CASCADE,
                                 related_name="industry_set")


class Question(models.Model):
    """A question in a survey"""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)


class Option(models.Model):
    """A multi-choice option available as a part of a survey question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=128)


class Submission(models.Model):
    """A set of answers a survey's questions."""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)


class Answer(models.Model):
    """An answer a survey's questions."""

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
