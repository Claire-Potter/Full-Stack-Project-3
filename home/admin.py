from django.contrib import admin
from .models import Contact, Verification


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    The Contact admin set up reads the Contact model and allows
    the admin user to delete contact requests.
    """
    list_display = ('name', 'email', 'created_on',)
    list_filter = ('created_on', 'name',)
    search_fields = ('name', 'email',)


admin.site.register(Verification)
