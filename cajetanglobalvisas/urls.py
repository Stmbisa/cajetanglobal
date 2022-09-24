from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views 
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/memberships/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('memberships/',include('memberships.urls')),
    path('users/', include('users.urls')),
    # path('register', user_views.register, name='register'),
    # path('login', user_views.loginView, name = 'login'),
    # path('logout', user_views.logOut, name = 'logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #settings.STATIC_ROOT=
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#to change this during production time 
