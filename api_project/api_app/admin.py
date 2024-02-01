from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Utilisateur, CustomUserAdmin)
admin.site.register(Song)
