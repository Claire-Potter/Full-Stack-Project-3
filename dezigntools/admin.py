from django.contrib import admin

from .models import (Survey, Question, Option, Submission, Answer,
                     DefaultQuestion, AgeRange, Gender, Industry)


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
    should not be deleted if set to True.
    """
    list_display = ('title', 'do_not_delete')
    search_fields = ['title', 'do_not_delete']
    list_filter = ('title', 'do_not_delete')


@admin.register(AgeRange)
class AgeRangeAdmin(admin.ModelAdmin):
    """
    Model created to store the age range choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('title', 'do_not_delete')
    search_fields = ['title', 'do_not_delete']
    list_filter = ('title', 'do_not_delete')


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    """
    Model created to store the age range choices.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('title', 'do_not_delete')
    search_fields = ['title', 'do_not_delete']
    list_filter = ('title', 'do_not_delete')


@admin.register(DefaultQuestion)
class DefaultQuestionAdmin(admin.ModelAdmin):
    """
    Model created to store the default questions answers.
    Admin can also edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('survey', 'name', 'email', 'do_not_delete')
    search_fields = ['survey', 'name', 'email', 'do_not_delete']
    list_filter = ('survey', 'name', 'email', 'do_not_delete')


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
    list_display = ('submission', 'option', 'do_not_delete')
    search_fields = ['submission', 'option', 'do_not_delete']
    list_filter = ('submission', 'option', 'do_not_delete')
