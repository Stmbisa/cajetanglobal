from django.urls import URLPattern, path
from .views import *

app_name = "memberships"
urlpatterns = [
    path('', membership_view, name='membership'),
    path ('profile_detail', profile, name='user_profile'),
    path ('profile/update', userprofileupdate, name='user_update'),
    path ('profile/files', userfileupload, name='user_files_upload'),
]
