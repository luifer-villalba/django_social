from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo')
    raw_id_fields = ('user',)