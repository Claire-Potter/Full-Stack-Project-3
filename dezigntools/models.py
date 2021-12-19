"""
Xperiencedezignwiz dezigntools app  models

The following site provided a Django project
blueprint to build a survey app. This was
followed alongside the git hub page. I then customised
the models to align with my
site's design and functionality.
https://mattsegal.dev/django-survey-project.html.

The Survey model is created to store the data for the
survey created by a user.

The Gender model is created to store the gender choices.
This is chosen as part of the survey within the default
questions section.

The AgeRange model is created to store the age range choices.
This is chosen as part of the survey within the default
questions section.

The Industry model is created to store the Industry choices.
This is chosen as part of the survey within the default
questions section.

The DefaultQuestion model is utilised to
store the default questions added to all surveys.
All user answers are saved to this model.

The Question model is used to store the questions
created by a user.

The Option model is used to store the multi-choice
options created by a user. .

The Submission model is utilised to store the set of answer
selections as answered by the user.

The Answer model is utilised to store the set of option
selections as answered by the user. T
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Survey(models.Model):
    """
    The Survey model is created to store the data for the
    survey created by a user. The title field stores
    the survey title. The survey image is a Cloudinary
    field to upload an image for the survey. Is_active
    indicates true if the survey has been activated,
    otherwise false. The creator is a forreignkey field
    which returns the username. Created_at will be the date
    and time that the survey was created. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """

    title = models.CharField(max_length=64)
    survey_image = CloudinaryField('image', default='efeeyko4svga74cweezl',
                                   blank=True,
                                   null=True)
    is_active = models.BooleanField(default=False)
    do_not_delete = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    # The string is set to return as the Survey title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class Gender(models.Model):
    """
    Model created to store the gender choices.
    This is chosen as part of the survey within the default
    questions section. The title contains the gender choice
    and the order_number is used to determine the order to
    sort the gender choices by. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    title = models.CharField(max_length=80)
    order_number = models.IntegerField()
    do_not_delete = models.BooleanField(default=True)

    class Meta:
        """
        The Meta determines the ordering of the
        gender choices according to order_number.
        """
        ordering = ["order_number"]

    # The string is set to return as the Gender title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class AgeRange(models.Model):
    """
    The AgeRange model is created to store the age range choices.
    This is chosen as part of the survey within the default
    questions section. The title contains the age range choice
    and the order_number is used to determine the order to
    sort the age ranges by choices by. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    title = models.CharField(max_length=80)
    order_number = models.IntegerField()
    do_not_delete = models.BooleanField(default=True)

    class Meta:
        """
        The Meta determines the ordering of the
        age range choices according to order_number.
        """
        ordering = ["order_number"]

    # The string is set to return as the AgeRange title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class Industry(models.Model):
    """
    The Industry model is created to store the Industry choices.
    This is chosen as part of the survey within the default
    questions section. The title field stores the Industry
    choice and is used to sorder the model by. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    title = models.CharField(max_length=250)
    do_not_delete = models.BooleanField(default=True)

    class Meta:
        """
        The Meta determines the ordering of the
        industry choices according to the title.
        """
        ordering = ["title"]

    # The string is set to return as the Industry title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class DefaultQuestion(models.Model):
    """
    The DefaultQuestion model is utilised to
    store the default questions added to all surveys.
    All user answers are saved to this model. The survey
    field is a ForeignKey field which is used to save the
    related survey, the name is the username, which is
    automaticall derived from the User,
    the email is the user email, which is  automatically derived
    from the User, the gender field contains the gender choices
    from the related Gender model, the age_range field contains the age_range
    choices from the related AgeRange model and the industry field
    contains the industry choices from the related Industry model.
    """

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
    do_not_delete = models.BooleanField(default=False)

    # The string is set to return as the Survey field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.survey) if self.survey else ' '


class Question(models.Model):
    """
    The Question model is used to store the questions
    created by a user. The survey field contains the
    related survey and the question field is utilised
    to capture and store the question.
    """

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    do_not_delete = models.BooleanField(default=False)

    # The string is set to return as the question field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.question) if self.question else ' '


class Option(models.Model):
    """
    The Option model is used to store the multi-choice
    options created by a user. The question field contains the
    related question and the option field is utilised
    to capture and store the options.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=128)
    do_not_delete = models.BooleanField(default=False)

    # The string is set to return as the option field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.option) if self.option else ' '


class Submission(models.Model):
    """
    The Submission model is utilised to store the set of answer
    selections as answered by the user. The survey field
    contains the related survey, the created_at field contains the
    date and time of creation and the is_complete field will be true
    if completed otherwise false.
    """

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)
    do_not_delete = models.BooleanField(default=False)

    # The string is set to return as the Survey field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.survey) if self.survey else ' '


class Answer(models.Model):
    """
    The Answer model is utilised to store the set of option
    selections as answered by the user. The submission field contains
    the related submission from the Submission model, the option field
    contains the options selected.
    """

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    do_not_delete = models.BooleanField(default=False)

    # The string is set to return as the Option field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.option) if self.option else ' '
