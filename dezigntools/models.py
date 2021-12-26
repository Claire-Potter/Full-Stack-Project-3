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

The Question model is used to store the questions
created by a user.

The AgeQuestion model is used to store the default
age question.

The GenderQuestion model is used to store the default
gender question.

The IndustryQuestion model is used to store the default
industry question.

The Option model is used to store the multi-choice
options created by a user. .

The Submission model is utilised to store the set of answer
selections as answered by the user.

The Answer model is utilised to store the set of option
selections as answered by the user.

The Default Answer model is utilised to store the s
et of default answers as answered by the user.
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Survey(models.Model):
    """
    The Survey model is created to store the data for the
    survey created by a user.
    """
    title = models.CharField(max_length=64)
    survey_image = CloudinaryField('image', default='son8liypgdn9yzc3lx7h',
                                   blank=True,
                                   null=True)
    is_active = models.BooleanField(default=False)
    deletable = models.BooleanField(default=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    # The string is set to return as the Survey title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class Question(models.Model):
    """
    The Question model is used to store the questions
    created by a user.
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=128)
    deletable = models.BooleanField(default=True, editable=False)

    # The string is set to return as the question field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.question) if self.question else ' '


class AgeQuestion(models.Model):
    """
    The AgeQuestion model is used to store the default
    age question.
    """
    age_question = models.CharField(max_length=128,
                                    default='Please select your age range:')
    deletable = models.BooleanField(default=False, editable=False)

    # The string is set to return as the question field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.age_question) if self.age_question else ' '


class GenderQuestion(models.Model):
    """
    The GenderQuestion model is used to store the default
    gender question.
    """
    gender_question = models.CharField(max_length=128,
                                       default='Please select your'
                                               ' preferred gender:')
    deletable = models.BooleanField(default=False, editable=False)

    # The string is set to return as the question field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.gender_question) if self.gender_question else ' '


class IndustryQuestion(models.Model):
    """
    The IndustryQuestion model is used to store the default
    industry question.
    """
    industry_question = models.CharField(max_length=128,
                                         default='Please select your'
                                                 ' Industry of employment:')
    deletable = models.BooleanField(default=False, editable=False)

    # The string is set to return as the question field
    # if it exists, else a blank field
    def __str__(self):
        return ('%s' % (self.industry_question)
                if self.industry_question else ' ')


class Option(models.Model):
    """
    The Option model is used to store the multi-choice
    options created by a user.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=128)
    deletable = models.BooleanField(default=True, editable=False)

    # The string is set to return as the option field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.option) if self.option else ' '


class AgeRange(models.Model):
    """
    The AgeRange model is created to store the age range choices.
    This is chosen as part of the survey within the default
    questions section.
    """
    title = models.CharField(max_length=80)
    order_number = models.IntegerField()
    deletable = models.BooleanField(default=False, editable=False)

    class Meta:
        """
        The Meta determines the ordering of the
        model according to order_number.
        """
        ordering = ['order_number']

    # The string is set to return as the AgeRange title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class Gender(models.Model):
    """
    Model created to store the gender choices.
    This is chosen as part of the survey within the default
    questions section.
    """
    title = models.CharField(max_length=80)
    order_number = models.IntegerField()
    deletable = models.BooleanField(default=False, editable=False)

    class Meta:
        """
        The Meta determines the ordering of the
        gender choices according to order_number.
        """
        ordering = ['order_number']

    # The string is set to return as the Gender title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class Industry(models.Model):
    """
    The Industry model is created to store the Industry choices.
    This is chosen as part of the survey within the default
    questions section.
    """
    title = models.CharField(max_length=250)
    deletable = models.BooleanField(default=False, editable=False)

    class Meta:
        """
        The Meta determines the ordering of the
        industry choices according to the title
        and the plural name.
        """
        ordering = ['title']
        verbose_name_plural = 'Industries'

    # The string is set to return as the Industry title field
    # if it exists, else a blank title
    def __str__(self):
        return '%s' % (self.title) if self.title else ' '


class DefaultOptions(models.Model):
    """
    The DefaultOptions model is utilised to
    store the default questions added to all surveys.
    As well as the default options.
    """

    survey = models.ForeignKey(Survey,
                               on_delete=models.CASCADE)

    age_question = models.ForeignKey(AgeQuestion, on_delete=models.CASCADE,
                                     related_name='agequestion_set')

    gender_question = models.ForeignKey(GenderQuestion,
                                        on_delete=models.CASCADE,
                                        related_name='genderquestion_set')

    industry_question = models.ForeignKey(IndustryQuestion,
                                          on_delete=models.CASCADE,
                                          related_name='industryquestion_set')

    age_ranges = models.ManyToManyField(AgeRange,
                                        related_name='age_ranges_set')

    genders = models.ManyToManyField(Gender, related_name='genders_set')

    industries = models.ManyToManyField(Industry,
                                        related_name='industries_set')
    deletable = models.BooleanField(default=True, editable=False)
    active = models.BooleanField(default=True, blank=False)

    class Meta:
        """
        The Meta determines the ordering of the
        model and the plural name.
        """
        ordering = ['survey']
        verbose_name_plural = 'Default Options'

    # The string is set to return as the Survey field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.survey) if self.survey else ' '


class Submission(models.Model):
    """
    The Submission model is utilised to store the set of answer
    selections as answered by the user.
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)
    deletable = models.BooleanField(default=True, editable=False)

    # The string is set to return as the Survey field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.survey) if self.survey else ' '


class Answer(models.Model):
    """
    The Answer model is utilised to store the set of option
    selections as answered by the user.
    """
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    deletable = models.BooleanField(default=True, editable=False)

    # The string is set to return as the Option field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.option) if self.option else ' '


class DefaultAnswers(models.Model):
    """
    The DefaultAnswers model is utilised to
    store the default questions answers.
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    age_range = models.ForeignKey(AgeRange,
                                  related_name='questions_age_ranges_set',
                                  on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, related_name='questions'
                                                    '_genders'
                                                    '_set',
                               on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry,
                                 related_name='questions_industries_set',
                                 on_delete=models.CASCADE)
    deletable = models.BooleanField(default=True, editable=False)

    class Meta:
        """
        The Meta determines the ordering of the
        model and the plural name.
        """
        ordering = ['submission']
        verbose_name_plural = 'Default Answers'

    # The string is set to return as the Survey field
    # if it exists, else a blank field
    def __str__(self):
        return '%s' % (self.survey) if self.survey else ' '
