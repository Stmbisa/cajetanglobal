from django.urls import URLPattern, path
from . import views


app_name = "accounts"
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgotPassword/', views.forgotPassword, name='forgotpassword'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    

    
]