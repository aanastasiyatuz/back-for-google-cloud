from django.contrib import admin
from .models import ProfileProvider, ProfileClient

admin.site.register(ProfileProvider)
admin.site.register(ProfileClient)