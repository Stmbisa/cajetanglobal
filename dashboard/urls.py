from django.urls import URLPattern, path
from django.conf import settings
from django.conf.urls.static import static
from . views import Profiles, Profile_detail, Profile_update, Profile_delete, dashboard, Profile_create,\
    Accounts_revenues, Accounts_revenue_detail, Accounts_revenue_create, Accounts_revenue_update, Accounts_revenue_delete, \
        Accounts_expenses, Accounts_expense_detail, Accounts_expense_create, Accounts_expense_update, Accounts_expense_delete
             #add_profile
app_name = "dashboard"
urlpatterns = [
    path ('', dashboard, name='dash_home'),
    path ('profiles/', Profiles.as_view(), name='profiles'),
    path ('profiles/<str:pk>', Profile_detail.as_view(), name='profile'),
    path ('profiles/<str:pk>/update/', Profile_update.as_view(), name='profile_update'),
    path ('profiles/<str:pk>/delete/', Profile_delete.as_view(), name='profile_delete'),
    path ('profiles/create/', Profile_create.as_view(), name='profile_create'),
    

    # all accounts
    path ('accounts/', Profiles.as_view(), name='accounts'),
    # accounts revenues 
   
    path ('accounts/revenues', Accounts_revenues.as_view(), name='revenues'),
    path ('accounts/revenues/<str:pk>', Accounts_revenue_detail.as_view(), name='revenue'),
    path ('accounts/revenues/<str:pk>/update/', Accounts_revenue_update.as_view(), name='revenue_update'),
    path ('accounts/revenues/<str:pk>/delete/', Accounts_revenue_delete.as_view(), name='revenue_delete'),
    path ('accounts/revenues/create/', Accounts_revenue_create.as_view(), name='revenue_create'),

    # accounts expenses 
    path ('accounts/expenses', Accounts_expenses.as_view(), name='expenses'),
    path ('accounts/expenses/<str:pk>', Accounts_expense_detail.as_view(), name='expense'),
    path ('accounts/expenses/<str:pk>/update/', Accounts_expense_update.as_view(), name='expense_update'),
    path ('accounts/expenses/<str:pk>/delete/', Accounts_expense_delete.as_view(), name='expense_delete'),
    path ('accounts/expenses/create/', Accounts_expense_create.as_view(), name='expense_create'),
    
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)