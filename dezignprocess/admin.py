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
from .models import Step, Comment, Tool, Progress, Resource, Image


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
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('title', 'deletable')
    search_fields = ['title', 'excerpt', 'deletable']
    list_filter = ('deletable',)
    summernote_fields = ('body')

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('title', 'slug', 'order_number',
                                           'added', 'list_number', 'deletable')
        return self.readonly_fields

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Tool)
class ToolAdmin(SummernoteModelAdmin):
    """
    The Tool admin set up reads the Tool model and allows
    the admin user to create a new tool by adding the
    required fields. Admin can also edit and delete.
    Django summernote is included to allow the admin user
    to style the body field.
    Cloudinary storage is utilised to store the images.
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('title', 'deletable')
    search_fields = ['title', 'deletable']
    summernote_fields = ('body',)
    list_filter = ('deletable',)
    exclude = ('slug', 'order_number')

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('title', 'slug', 'order_number',
                                           'deletable')
        return self.readonly_fields


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    """
    The Progress admin set up reads the Progress model and allows
    the admin user to delete progress input. No approval of progress
    status is required as user progress status will only display to the
    user themself. The default 'Not Started' progress status was
    captured by the admin user from this screen. No additional
    progress statuses should be captured by the admin user.
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('progress', 'step', 'updated_on', 'name',
                    'deletable')
    list_filter = ('updated_on', 'step', 'deletable')
    search_fields = ('name', 'email', 'progress', 'deletable')
    exclude = ('username',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('name', 'email', 'step',
                                           'updated_on', 'progress')
        return self.readonly_fields

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    The Comment admin set up reads the Comment model and allows
    the admin user to delete comments. No approval of comments
    is required as user comments will only display to the
    user themself. Admin should not capture comments.
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('name', 'body', 'step', 'created_on',
                    'deletable')
    list_filter = ('created_on', 'step', 'deletable')
    search_fields = ('name', 'email', 'body', 'deletable')
    exclude = ('username',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('name', 'email', 'step',
                                           'created_on', 'body')
        return self.readonly_fields

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Resource)
class ResourceAdmin(AdminVideoMixin, admin.ModelAdmin):
    """
    The Resource admin set up reads the Resource model and allows
    the admin user to create a new Resource by adding the
    required fields. Admin can also edit and delete.
    AdminVideoMixin creates a preview od the video
    Embed video is utilised to store the video.
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('video_name', 'video_url', 'deletable')
    search_fields = ['video_name', 'deletable']
    list_filter = ('video_name', 'video_url', 'deletable')
    exclude = ('order_number', 'added')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('video_name',)
        return self.readonly_fields

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Image)
class ImageAdmin(AdminVideoMixin, admin.ModelAdmin):
    """
    The Images admin set up reads the Images model and allows
    the admin user to create a new Image by adding the
    required fields. Admin can also edit and delete.
    Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('category', 'title', 'name', 'deletable')
    search_fields = ['title', 'name', 'deletable']
    list_filter = ('category', 'title', 'deletable')
    exclude = ('order_number', 'added')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('title', 'category',)
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
