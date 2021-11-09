from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Step(models.Model):
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    order_number = models.IntegerField()

    class Progress(models.TextChoices):
        NotStarted = 'NS', ('Not Started')
        InProgress = 'IP', ('In Progress')
        Completed = 'C', ('Completed')
        Revisiting = 'R', ('Revisiting')

    progress = models.CharField(
        max_length=10,
        choices=Progress.choices,
        default=Progress.NotStarted,
    )

    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return self.title


class KnowledgeResource(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name="resources")
    title = models.CharField(max_length=80, unique=True)
    excerpt = models.TextField(blank=True)
    order_number = models.IntegerField()

    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return self.title


class Template(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name="templates")
    title = models.CharField(max_length=80, unique=True)
    excerpt = models.TextField(blank=True)
    order_number = models.IntegerField()

    class Meta:
        ordering = ["order_number"]

    def __str__(self):
        return f"Template: {self.title}"
