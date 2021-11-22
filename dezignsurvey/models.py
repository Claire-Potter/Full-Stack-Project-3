from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Gender(models.Model):
    """
    Model created to store the gender choices.
    """
    title = models.CharField(max_length=80, unique=True)
    order_number = models.IntegerField()

    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


class AgeRange(models.Model):
    """
    Model created to store the age_range choices.
    """
    title = models.CharField(max_length=80, unique=True)
    order_number = models.IntegerField()

    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


class Survey(models.Model):
    survey_title = models.CharField(max_length=80)
    survey_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=80, unique=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="surveys",
        default="1")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    gender = models.ForeignKey(
        Gender, on_delete=models.CASCADE,
        related_name="survey_answers")
    age_range = models.ForeignKey(
        AgeRange, on_delete=models.CASCADE,
        related_name="survey_answers")
    job_title = models.TextField()
    industry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
   
    def __str__(self):
        return '%s' % (self.survey_title)
