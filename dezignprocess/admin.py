"""
Xperiencedezignwiz dezignprocess app admin Configuration

Set up for the dezignprocess models display within the
django admin centre.
The Step admin set up reads the Step model and allows
the admin user to create a new step by adding the
required fields. Admin can also edit and delete.
The Tool admin set up reads the Tool model and allows
the admin user to create a new tool by adding the
required fields. Admin can also edit and delete.
The Comment admin set up reads the Comment model and allows
the admin user to delete comments. No approval of comments
is required as user comments will only display to the
user themself. Admin should not capture comments.
The Progress admin set up reads the Progress model and allows
the admin user to delete progress input. No approval of progress
status is required as user progress status will only display to the
user themself. The default 'Not Started' progress status was
captured by the admin user from this screen. No additional
progress statuses should be captured by the admin user.
The Resource admin set up reads the Resource model and allows
the admin user to create a new Resource by adding the
required fields. Admin can also edit and delete.
The Images admin set up reads the Images model and allows
the admin user to create a new Image by adding the
required fields. Admin can also edit and delete.
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from embed_video.admin import AdminVideoMixin
from .models import Step, Comment, Tool, Progress, Resource, Images


@admin.register(Step)
class StepAdmin(SummernoteModelAdmin):
    """
    The Step admin set up reads the Step model and allows
    the admin user to create a new step by adding the
    required fields. Admin can also edit and delete.
    Django summernote is included to allow the admin user
    to style the body field.
    Django embed video is utilised to store video links.
    Cloudinary storage is utilised to store the images.
    """
    summernote_fields = '__all__'
    list_display = ('title', 'slug', 'added')
    search_fields = ['title', 'excerpt']
    list_filter = ('added',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):
    """
    The Tool admin set up reads the Tool model and allows
    the admin user to create a new tool by adding the
    required fields. Admin can also edit and delete.
    Django summernote is included to allow the admin user
    to style the body field.
    Cloudinary storage is utilised to store the images.
    """
    summernote_fields = '__all__'
    list_display = ('title', 'slug',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    """
    The Progress admin set up reads the Progress model and allows
    the admin user to delete progress input. No approval of progress
    status is required as user progress status will only display to the
    user themself. The default 'Not Started' progress status was
    captured by the admin user from this screen. No additional
    progress statuses should be captured by the admin user.
    """
    list_display = ('progress', 'step', 'updated_on', 'name',)
    list_filter = ('updated_on', 'step',)
    search_fields = ('name', 'email', 'progress',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    The Comment admin set up reads the Comment model and allows
    the admin user to delete comments. No approval of comments
    is required as user comments will only display to the
    user themself. Admin should not capture comments.
    """
    list_display = ('name', 'body', 'step', 'created_on',)
    list_filter = ('created_on', 'step',)
    search_fields = ('name', 'email', 'body',)


@admin.register(Resource)
class ResourceAdmin(AdminVideoMixin, admin.ModelAdmin):
    """
    The Resource admin set up reads the Resource model and allows
    the admin user to create a new Resource by adding the
    required fields. Admin can also edit and delete.
    AdminVideoMixin creates a preview od the video
    Embed video is utilised to store the video.
    """
    list_display = ('video_name', 'video_url')
    search_fields = ['video_name']
    list_filter = ('video_name', 'video_url')


@admin.register(Images)
class ImageAdmin(AdminVideoMixin, admin.ModelAdmin):
    """
    The Images admin set up reads the Images model and allows
    the admin user to create a new Image by adding the
    required fields. Admin can also edit and delete.
    """
    list_display = ('category', 'title', 'name')
    search_fields = ['title', 'name']
    list_filter = ('category', 'title')
