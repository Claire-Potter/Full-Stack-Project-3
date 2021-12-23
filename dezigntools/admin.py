"""
The Survey model is created to store the data for the
survey created by a user. Admin can also edit and delete.

The Gender model created to store the gender choices.

AgeRange model created to store the age range choices.

Industry model created to store the age range choices.

Questions model created to store the questions created
by the users.
Admin can also edit and delete.

The AgeQuestion model is used to store the default
age question.

The GenderQuestion model is used to store the default
gender question

The IndustryQuestion model is used to store the default
industry question.

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
                    'created_at', 'deletable')
    search_fields = ['title', 'is_active', 'deletable']
    list_filter = ('deletable', 'creator', 'created_at')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    """
    Model created to store the gender choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True. It is
    """
    search_fields = ['title', 'deletable']
    list_filter = ('title', 'deletable')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AgeRange)
class AgeRangeAdmin(admin.ModelAdmin):
    """
    Model created to store the age range choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True. It is
    also marked as read_only.
    """
    list_display = ('title', 'deletable')
    search_fields = ['title', 'deletable']
    list_filter = ('title', 'deletable')
    readonly_fields = ['title']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    """
    Model created to store the age range choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True. It is also
    marked as read_only
    """
    list_display = ('title', 'deletable')
    search_fields = ['title', 'deletable']
    list_filter = ('title', 'deletable')
    readonly_fields = ['title']

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Model created to store the questions created
    by the users.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('question', 'survey', 'deletable')
    search_fields = ['question', 'survey', 'deletable']
    list_filter = ('question', 'survey', 'deletable')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(AgeQuestion)
class AgeQuestionAdmin(admin.ModelAdmin):
    """
    Model to store the age question.
    It is ready only
    """
    list_display = ('age_question', 'deletable')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(GenderQuestion)
class GenderQuestionAdmin(admin.ModelAdmin):
    """
    Model to store the gender question.
    It is ready only
    """
    list_display = ('gender_question', 'deletable')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(IndustryQuestion)
class IndustryQuestionAdmin(admin.ModelAdmin):
    """
    Model to store the age question.
    It is ready only
    """
    list_display = ('industry_question', 'deletable')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


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
                    'deletable')
    search_fields = ['survey', 'deletable']
    list_filter = ('survey', 'age_question', 'gender_question',
                   'industry_question', 'deletable')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    """
    Model created to store the option answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('question', 'option', 'deletable')
    search_fields = ['question', 'option', 'deletable']
    list_filter = ('question', 'option', 'deletable')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """
    Model created to store the submissions.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('survey', 'created_at', 'is_complete',
                    'deletable')
    search_fields = ['survey', 'created_at', 'is_complete',
                     'deletable']
    list_filter = ('survey', 'created_at', 'is_complete',
                   'deletable')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
    Model created to store the answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('submission', 'option', 'deletable')
    search_fields = ['submission', 'option']
    list_filter = ('submission', 'option')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(DefaultAnswers)
class DefaultAnswerAdmin(admin.ModelAdmin):
    """
    Model created to store the default answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('submission', 'survey', 'deletable')
    search_fields = ['submission', 'survey', 'deletable']
    list_filter = ('submission', 'survey', 'deletable')

    def has_add_permission(self, request, obj=None):
        return False
