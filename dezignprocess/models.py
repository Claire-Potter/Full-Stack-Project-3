from django.db import models
# from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


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
    excerpt = models.TextField(blank=True)
    order_number = models.IntegerField()

    class Progress(models.TextChoices):
        """
        Progress class to create the text field choices for the progress
        dropdown within the Step Model.
        """
        NOT_STARTED = 'NS', ('Not Started')
        IN_PROGRESS = 'IP', ('In Progress')
        COMPLETED = 'C', ('Completed')
        REVISITING = 'R', ('Revisiting')

    progress = models.CharField(
        max_length=10,
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


class KnowledgeResource(models.Model):
    """
    Model created to store the various resources utilised
    within the site. These are learning resource videos,
    created by Code Institute to upskill students on the
    various stages within the Design Thinking Process.
    The resources arfe assigned against the relevant step
    within the process.
    """
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name="resources")
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


class Template(models.Model):
    """
    Model created to store the document templates per step.
    These are templates utilised to create the necessary
    Design Thinking support documents per step.
    """
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name="templates")
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
        return f"Template: {self.title}"
