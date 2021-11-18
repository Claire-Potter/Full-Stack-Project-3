from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


class KnowledgeResource(models.Model):
    """
    Model created to store the various resources utilised
    within the site. These are learning resource videos,
    created by Code Institute to upskill students on the
    various stages within the Design Thinking Process.
    The resources arfe assigned against the relevant step
    within the process.
    """
    title = models.CharField(max_length=80, unique=True)
    excerpt = models.TextField(blank=True)
    order_number = models.IntegerField()
    video = EmbedVideoField(blank=True)

    class Meta:
        """
        Meta created to order the Step Model according
        to order number assigned.
        """
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


class Template(models.Model):
    """
    Model created to store the document templates per step.
    These are templates utilised to create the necessary
    Design Thinking support documents per step.
    """
    title = models.CharField(max_length=80, unique=True)
    excerpt = models.TextField(blank=True)
    order_number = models.IntegerField()

    class Meta:
        """
        Meta created to order the Step Model according
        to order number assigned.
        """
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


class Step(models.Model):
    """
    Model created to store the data required for creating
    the different Steps within the Design Thinking Process.
    Steps include: Getting Started, Empathy, Define, Ideate,
    Prototype, Test and Finishing Off.
    """
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    step_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    order_number = models.IntegerField()
    resources = models.ManyToManyField(KnowledgeResource)
    templates = models.ManyToManyField(Template)
    list_number = models.IntegerField(
        default="1",)

    class Progress(models.TextChoices):
        """
        Progress class to create the text field choices for the progress
        dropdown within the Step Model.
        """
        NOT_STARTED = 'Not Started', ('0')
        IN_PROGRESS = 'In Progress', ('1')
        COMPLETED = 'Completed', ('2')
        REVISITING = 'Revisiting', ('3')

    progress = models.CharField(
        max_length=15,
        choices=Progress.choices,
        default=Progress.NOT_STARTED,
    )

    class Meta:
        """
        Meta created to order the Step Model according
        to order number assigned.
        """
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)

    def number_of_resources(self):
        return '%s' % (self.resources.count())

    def number_of_templates(self):
        return '%s' % (self.templates.count())

    def resources_as_list(self):
        return '-'.join([str(resource) for resource in self.resources.all()])

    def templates_as_list(self):
        return '-'.join([str(template) for template in self.templates.all()])


class Comment(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name="comments")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments",
        default="1"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ["-created_on"]


def __str__(self):
    return f"Comment {self.body} by {self.name}"
