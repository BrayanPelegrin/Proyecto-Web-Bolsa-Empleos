from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Owns
from .models import UserAccount

class AccountAdmin(UserAdmin):
    """ Account admin for django-admin """
    list_display = (
        'username', 'is_staff', 'is_active', 'is_superuser', 'date_joined'
    )
    list_display_links = ('username',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()

admin.site.register(UserAccount, AccountAdmin)
