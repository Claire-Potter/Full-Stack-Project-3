from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Step, Comment, Tool, Progress


@admin.register(Step)
class StepAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title', 'slug', 'added',)
    search_fields = ['title', 'excerpt']
    list_filter = ('added',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('step', 'title', 'slug',)
    search_fields = ['title', 'step', ]
    list_filter = ('title', 'step',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('progress', 'step', 'updated_on', 'name',)
    list_filter = ('updated_on', 'step',)
    search_fields = ('name', 'email', 'progress',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'step', 'created_on',)
    list_filter = ('created_on', 'step',)
    search_fields = ('name', 'email', 'body',)
