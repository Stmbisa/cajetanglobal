from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    # path('accounts/', include('users.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('memberships/',include('memberships.urls')),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #settings.STATIC_ROOT=
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#to change this during production time 
