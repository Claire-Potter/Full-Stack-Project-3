"""
The Survey model is created to store the data for the
survey created by a user. Admin can also edit and delete.

The Gender model created to store the gender choices.
Admin can also edit and delete.

AgeRange model created to store the age range choices.
Admin can also edit and delete.

Industry model created to store the age range choices.
Admin can also edit and delete.

Questions model created to store the questions created
by the users.
Admin can also edit and delete.

The AgeQuestion model is used to store the default
age question.
Admin can also edit and delete.

The GenderQuestion model is used to store the default
gender question
Admin can also edit and delete.

The IndustryQuestion model is used to store the default
industry question.
Admin can also edit and delete.

Option model created to store the option answers.
Admin can also edit and delete.

Submission model created to store the submissions.
Admin can also edit and delete.

Answer model created to store the answers.
Admin can also edit and delete.

The Default Answer model is utilised to store the
set of default answers as answered by the user.
Admin can also edit and delete
"""
from django.contrib import admin
from .models import (Survey, Question, Option, Submission, Answer,
                     AgeRange, Gender, Industry, AgeQuestion,
                     GenderQuestion, IndustryQuestion,
                     DefaultOptions, DefaultAnswers)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """
    The Survey model is created to store the data for the
    survey created by a user. Admin can also edit and delete.
    Cloudinary storage is utilised to store the images.
    Do not delete field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('title', 'is_active', 'creator',
                    'created_at', 'do_not_delete')
    search_fields = ['title', 'is_active', 'do_not_delete']
    list_filter = ('do_not_delete', 'creator', 'created_at')


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    """
    Model created to store the gender choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True. It is
    """
    search_fields = ['title', 'do_not_delete']
    list_filter = ('title', 'do_not_delete')
    readonly_fields = ['title']


@admin.register(AgeRange)
class AgeRangeAdmin(admin.ModelAdmin):
    """
    Model created to store the age range choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True. It is
    also marked as read_only.
    """
    list_display = ('title', 'do_not_delete')
    search_fields = ['title', 'do_not_delete']
    list_filter = ('title', 'do_not_delete')
    readonly_fields = ['title']


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    """
    Model created to store the age range choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True. It is also
    marked as read_only
    """
    list_display = ('title', 'do_not_delete')
    search_fields = ['title', 'do_not_delete']
    list_filter = ('title', 'do_not_delete')
    readonly_fields = ['title']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Model created to store the questions created
    by the users.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('question', 'survey', 'do_not_delete')
    search_fields = ['question', 'survey', 'do_not_delete']
    list_filter = ('question', 'survey', 'do_not_delete')


@admin.register(AgeQuestion)
class AgeQuestionAdmin(admin.ModelAdmin):
    """
    Model to store the age question.
    It is ready only
    """
    list_display = ('age_question', 'do_not_delete')
    readonly_fields = ['age_question']


@admin.register(GenderQuestion)
class GenderQuestionAdmin(admin.ModelAdmin):
    """
    Model to store the gender question.
    It is ready only
    """
    readonly_fields = ['gender_question']
    list_display = ('gender_question', 'do_not_delete')


@admin.register(IndustryQuestion)
class IndustryQuestionAdmin(admin.ModelAdmin):
    """
    Model to store the age question.
    It is ready only
    """
    readonly_fields = ['industry_question']
    list_display = ('industry_question', 'do_not_delete')


@admin.register(DefaultOptions)
class DefaultOptionsAdmin(admin.ModelAdmin):
    """
    Model created to store the default options and answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('survey', 'age_question', 'gender_question',
                    'industry_question',
                    'do_not_delete')
    search_fields = ['survey', 'do_not_delete']
    list_filter = ('survey', 'age_question', 'gender_question',
                   'industry_question', 'do_not_delete')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    """
    Model created to store the option answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('question', 'option', 'do_not_delete')
    search_fields = ['question', 'option', 'do_not_delete']
    list_filter = ('question', 'option', 'do_not_delete')


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """
    Model created to store the submissions.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('survey', 'created_at', 'is_complete',
                    'do_not_delete')
    search_fields = ['survey', 'created_at', 'is_complete',
                     'do_not_delete']
    list_filter = ('survey', 'created_at', 'is_complete',
                   'do_not_delete')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Model created to store the answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('submission', 'option')
    search_fields = ['submission', 'option']
    list_filter = ('submission', 'option')


@admin.register(DefaultAnswers)
class DefaultAnswerAdmin(admin.ModelAdmin):
    """
    Model created to store the default answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('submission', 'survey')
    search_fields = ['submission', 'survey']
    list_filter = ('submission', 'survey')
