from django.urls import URLPattern, path
from .views import register, membership_view, loginView, logOut

app_name = "memberships"
urlpatterns = [
    path('', membership_view, name='membership'),
    path('register', register, name='register'),
    path('login', loginView, name='login'),
    path('logout', logOut, name='logout'),
]
