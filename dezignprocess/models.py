"""
Xperiencedezignwiz dezignprocess app Model Configuration

The Step and Comment models were created according to the
Code Institute 'I Think Therefore I Blog' project but fully
customised for purpose.

The Image model is created to house all of the images
utilised by thw dezignprocess app.

The Resource Model is created to house the videos displayed
on the step_detail page.

The Tool Model is created to house the tools per step, which are
linked to from the step_detail page.

The Step Model is created to store the data required for creating
the different Steps within the Design Thinking Process.

The Progress Model is created to create and store a progress status.
The Comment Model is created to create and store a comment.

Models for the dezignprocess app to be rendered by dezignprocess/views.py
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from embed_video.fields import EmbedVideoField


class Image(models.Model):
    """
    The Image class to upload and store an image to Cloudinary,
    provide the alt / aria-label text using the name field.
    """
    name = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image', default='placeholder',
                            blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    order_number = models.IntegerField()
    deletable = models.BooleanField(default=True, editable=False)

    class ImageCategory(models.TextChoices):
        """
        ImageCategory class to create the text field choices for the
        category dropdown within the Image Model. Featured - images to
        be selected through the feature_image field within the Step
        Model, Step - images to be selected through the step_image
        field within the Step Model, Tool - images to be selected
        within the Tool Model image field and Other for any other
        images possibly added.
        """
        FEATURED = 'Featured', ('Featured')
        STEP = 'Step', ('Step')
        TOOL = 'Tool', ('Tool')
        OTHER = 'Other', ('Other')

    category = models.CharField(max_length=15, choices=ImageCategory.choices,
                                default=ImageCategory.OTHER,)

    class Meta:
        """
        Meta created to order the Image Model according
        to the order_number. It also determines the latest
        entry saved to the model referring to the added date.
        """
        ordering = ['order_number']
        get_latest_by = ['added']

    # The string is set to return as the Image title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class Resource(models.Model):
    """
    Utilised to store the videos displayed within
    the resources section on the step detail page.
    """
    video_name = models.CharField(max_length=100, blank=True,
                                  default='placeholder')
    video_url = EmbedVideoField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    order_number = models.IntegerField()
    deletable = models.BooleanField(default=True, editable=False)

    class Meta:
        """
        Meta created to order the Resource Model according
        to the order_number.
        """
        ordering = ['order_number']

    # The string is set to return the Video Name field if it exists
    #  else a blank string
    def __str__(self):
        return str(self.video_name) if self.video_name else ' '


class Tool(models.Model):
    """
    Utilised to store the data and
    create the view using the step_tool.html template.
    """
    title = models.CharField(max_length=80, unique=True,
                             default='placeholder')
    slug = models.SlugField(max_length=80, default='steps_document')
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE,
                              related_name='tool_image',
                              default='1')
    order_number = models.IntegerField()
    deletable = models.BooleanField(default=False)

    class Meta:
        """
        Meta created to order the Tools Model according
        to order number assigned.
        """
        ordering = ['order_number']

    # The string is set to return the Title field if it exists
    #  else a blank string
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class Step(models.Model):
    """
    Model created to store the data required for creating
    the different Steps within the Design Thinking Process.
    """
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    feature_image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='featured_image',
        default='0')
    steps_image = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='step_image',
        default='1')
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    order_number = models.IntegerField()
    resources = models.ManyToManyField(
        Resource, related_name='resource', blank=True)
    added = models.DateTimeField(auto_now_add=True)
    tools = models.ManyToManyField(
        Tool, related_name='tool', blank=True)
    list_number = models.IntegerField(
        default='0')
    deletable = models.BooleanField(default=False)

    class Meta:
        """
        Meta created to order the Step Model according
        to order number assigned.
        """
        ordering = ['order_number']

    # The string is set to return the Title field if it exists
    #  else a blank string
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '

    def number_of_tools(self):
        """
        A count of the number_of_tools by counting
        the number of tools selected in the tools
        field and returning it as an integer. This is
        displayed through the first.html template and the
        next.html template
        """
        return self.tools.count()

    def number_of_resources(self):
        """
        A count of the number_of_resources by counting
        the number of resources selected in the resources
        field and returning it as an integer. This is
        displayed through the first.html template and the
        next.html template
        """
        return self.resources.count()


class Progress(models.Model):
    """
    Model created to store the data required to display and
    update the progress status per step.
    """
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name='progress')
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='progress',
        default='1')
    name = models.CharField(max_length=80, default='username')
    email = models.EmailField(blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    deletable = models.BooleanField(default=True, editable=False)

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
        Meta created to order the Progress Model according
        to the updated_on field. It also determines the latest
        entry per step saved to the model. The verbose_name_plural
        field is used to set the plural name as Progress so that
        it does not reflect as Progresss in the admin panel.
        """
        ordering = ['updated_on']
        get_latest_by = ['updated_on']
        verbose_name_plural = 'Progress'

    # The string is set to return the Progress field if it exists
    #  else a blank string
    def __str__(self):
        return '%s' % (self.progress) if self.progress else ' '


class Comment(models.Model):
    """
    Model created to store the design thinking comments
    created by users per step.
    These comments users add as they progress through
    the various steps.
    """
    step = models.ForeignKey(Step, on_delete=models.CASCADE,
                             related_name='comments')
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        default='1'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    deletable = models.BooleanField(default=True, editable=False)

    class Meta:
        """
        Meta created to order the Comments Model according
        to the created on date.
        """
        ordering = ['-created_on']

    # The string is set to return the Comment body field and
    #  the Comment name field if they exist
    #  else a blank string
    def __str__(self):
        return (f'Comment {self.body} by {self.name}'
                if self.body and self.name else ' ')
