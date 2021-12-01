from django.contrib import admin
from .models import Step, Comment, Tool
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
    list_filter = ('step', 'title')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'step', 'created_on',)
    list_filter = ('created_on', 'step',)
    search_fields = ('name', 'email', 'body')
    # actions = ['approve_comments']

    # def approve_comments(self, request, queryset):
    # queryset.update(approved=True)
