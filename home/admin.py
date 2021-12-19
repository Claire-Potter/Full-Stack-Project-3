"""
Xperiencedezignwiz home app  adminconfiguration
"""
from django.contrib import admin
from .models import Home, Contact, Verification


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    The Contact admin set up reads the Contact model and allows
    the admin user to read and delete contact requests. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('name', 'email', 'created_on',
                    'do_not_delete')
    list_filter = ('created_on', 'name', 'do_not_delete')
    search_fields = ('name', 'email', 'do_not_delete')


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    """
    The Home admin set up reads the Home model and allows
    the admin user to create, edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('name', 'created_on',
                    'do_not_delete')
    list_filter = ('created_on', 'name', 'do_not_delete')
    search_fields = ('name', 'created_on', 'do_not_delete')


@admin.register(Verification)
class Verification(admin.ModelAdmin):
    """
    The Verification admin set up reads the Verification model and allows
    the admin user to create, edit and delete records. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('verification', 'updated_on',
                    'do_not_delete')
    list_filter = ('updated_on', 'do_not_delete')
    search_fields = ('verification', 'updated_on', 'do_not_delete')
