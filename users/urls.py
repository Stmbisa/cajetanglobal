from django.conf.urls import url, include
# from registration.views import RegistrationView
from django.urls import path, include
from .views import UserRegistrationView

from .forms import RegisterUserCreationForm   


app_name= 'users'
urlpatterns = [
    # path('register/', UserRegistrationView.as_view(form_class=RegisterUserCreationForm),
    #     name='accounts:logout',),
    # url('', include('registration.backends.default.urls')),
]