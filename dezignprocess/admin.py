from django.contrib import admin
from .models import Step, Comment, Tool, Progress
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Step)
class StepAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title', 'slug', 'progress', 'added')
    search_fields = ['title', 'excerpt']
    list_filter = ('progress', 'added')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('step', 'title', 'slug')
    search_fields = ['title', 'step']
    list_filter = ('title', 'step')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress', 'step', 'updated_on',)
    list_filter = ('updated_on', 'step',)
    search_fields = ('name', 'email', 'progress')

    # actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    # queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'step', 'created_on',)
    list_filter = ('created_on', 'step',)
    search_fields = ('name', 'email', 'body')
