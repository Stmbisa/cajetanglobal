from urllib import request
from .models import Profile,  User, Announcement

from django.contrib import admin
from .forms import AnnouncementCreateForm,ProfileCreateForm

class ProfileCreateAdmin(admin.ModelAdmin):
    list_display  = ['first_name', 'last_name', 'email','phonenumber','country_of_destination']
    form = ProfileCreateForm()
    list_filter =  ['country_of_destination']
    search_fields =['first_name', 'last_name','phonenumber', 'email']

class AnnouncementCreateFormAdmin(admin.ModelAdmin):
    list_display  = '__all__'
    form = AnnouncementCreateForm()
    list_filter =  '__all__'
    search_fields = '__all__'

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Announcement)
