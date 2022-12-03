from urllib import request
from .models import Profile,  User, Announcement
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .forms import AnnouncementCreateForm,ProfileCreateForm

class UsersAdmin(UserAdmin):
    list_display = ('avatar','first_name', 'last_name','email', 'gender','phone','country_of_orgin', 'country_of_destination', 'nationality', 'next_of_kin', 'next_of_kin_phone_number')
    list_display_links = ('email','first_name', 'last_name',  )
    readonly_fields= ('is_verified','last_login' )
    ordering = ('-date_joined',)

    filter_horizontal=()
    list_filter = ()
    fieldsets= ()



class ProfileCreateAdmin(admin.ModelAdmin):
    list_display  = ['first_name', 'last_name', 'email','phonenumber','country_of_destination', ]
    form = ProfileCreateForm
    list_filter =  ['country_of_destination']
    search_fields =['first_name', 'last_name','phonenumber', 'email', 'country_of_destination']

class AnnouncementCreateFormAdmin(admin.ModelAdmin):
    list_display  = '__all__'
    form = AnnouncementCreateForm
    list_filter =  '__all__'
    search_fields = '__all__'

admin.site.register(User, UsersAdmin)
admin.site.register(Profile, ProfileCreateAdmin)
admin.site.register(Announcement)
