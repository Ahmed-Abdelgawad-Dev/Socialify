from django.contrib import admin
from .models import Profile
# from .models import Contact
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ['user_from', 'user_to', 'created']
