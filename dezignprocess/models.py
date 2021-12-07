from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField


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
    resources = models.IntegerField(blank=True)
    video_url = EmbedVideoField(blank=True)
    video_name = models.CharField(max_length=80, default='placeholder')
    video_two_url = EmbedVideoField(blank=True)
    video_two_name = models.CharField(max_length=80, default='placeholder')
    video_three_url = EmbedVideoField(blank=True)
    video_three_name = models.CharField(max_length=80, default='placeholder')
    added = models.DateTimeField(auto_now_add=True)
    tools = models.IntegerField(blank=True)
    username_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="username_step",
        default="1")
    name = models.CharField(max_length=80, blank=True)
    list_number = models.IntegerField(
        default='1')

    class Meta:
        """
        Meta created to order the Step Model according
        to order number assigned.
        """
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


class Progress(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name="progress")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="progress",
        default="1")
    name = models.CharField(max_length=80, default="username")
    email = models.EmailField()
    updated_on = models.DateTimeField(auto_now_add=True)

    class ProgressStatus(models.TextChoices):
        """
        Progress class to create the text field choices for the progress
        dropdown within the Step Model.
        """
        NOT_STARTED = 'Not Started', ('Not Started')
        IN_PROGRESS = 'In Progress', ('In Progress')
        COMPLETED = 'Completed', ('Completed')
        REVISITING = 'Revisiting', ('Revisiting')

    progress = models.CharField(max_length=15, choices=ProgressStatus.choices,
                                default=ProgressStatus.NOT_STARTED,)

    class Meta:
        """
        Meta created to order the Step Model according
        to order number assigned.
        """
        ordering = ["updated_on"]
        get_latest_by = ["updated_on"]

    def __str__(self):
        return '%s' % (self.progress)


class Tool(models.Model):
    """
    Model created to store the design thinking recommended tools per step.
    These are tools utilised to provide advice on help to complete each step.
    """
    title = models.CharField(max_length=80, unique=True, default='placeholder')
    slug = models.SlugField(max_length=80, default='steps_document')
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    template_image = CloudinaryField('image', default='placeholder')
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name="tool")
    order_number = models.IntegerField()

    class Meta:
        """
        Meta created to order the Step Model according
        to order number assigned.
        """
        ordering = ["order_number"]

    def __str__(self):
        return '%s' % (self.title)


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
