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
                    'deletable')
    list_filter = ('created_on', 'name', 'deletable')
    search_fields = ('name', 'email', 'deletable')


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    """
    The Home admin set up reads the Home model and allows
    the admin user to create, edit and delete. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('name', 'created_on',
                    'deletable')
    list_filter = ('created_on', 'name', 'deletable')
    search_fields = ('name', 'created_on', 'deletable')

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Verification)
class Verification(admin.ModelAdmin):
    """
    The Verification admin set up reads the Verification model and allows
    the admin user to create, edit and delete records. Do not delete
    field is added to indicate that the saved data
    should not be deleted if set to True.
    """
    list_display = ('verification', 'updated_on',
                    'deletable')
    list_filter = ('updated_on', 'deletable')
    search_fields = ('verification', 'updated_on', 'deletable')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
