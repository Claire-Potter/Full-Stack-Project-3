from django.contrib import admin
from .models import Step, Comment, Template

admin.site.register(Step)
admin.site.register(Template)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'step', 'created_on',)
    list_filter = ('created_on', 'step',)
    search_fields = ('name', 'email', 'body')
    #actions = ['approve_comments']

    #def approve_comments(self, request, queryset):
        #queryset.update(approved=True)
