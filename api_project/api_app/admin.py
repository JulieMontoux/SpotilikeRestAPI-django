from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Utilisateur)
admin.site.register(Song)
