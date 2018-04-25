from django.contrib import admin

'''
    Tagen från https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
'''
"""Integrate with admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User
from .models import Manager
from .models import Message


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password','first_name')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name','last_name','phone','has_logged_in'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass
