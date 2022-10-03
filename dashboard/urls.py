from django.urls import URLPattern, path
from django.conf import settings
from django.conf.urls.static import static
from . views import profiles, Profile_detail, Profile_update, Profile_delete, dashboard, Profile_create,\
    AccountsRevenues, revenue_detail_view, AccountsRevenueCreate, AccountsRevenueUpdate, AccountsRevenue_delete, \
        AccountsExpenses, AccountsExpenseDetail, AccountsExpenseCreate, AccountsExpenseUpdate, AccountsExpenseDelete,userprofileupdate
             #add_profile
app_name = "dashboard"
urlpatterns = [
    path ('', dashboard, name='dash_home'),
    path ('profiles/', profiles, name='profiles'),
    path ('profiles/<str:pk>', Profile_detail.as_view(), name='profile'),
    path ('profiles/<str:pk>/update/', Profile_update.as_view(), name='profile_update'),
    path ('profiles/<str:pk>/delete/', Profile_delete.as_view(), name='profile_delete'),
    path ('profiles/create/', Profile_create.as_view(), name='profile_create'),
    path ('profile', userprofileupdate, name='user_update'),
    

    # all accounts
    # path ('accounts/', Profiles.as_view(), name='accounts'),
    # accounts revenues 
   
    path ('accounts/revenues', AccountsRevenues.as_view(), name='revenues'),
    path ('accounts/revenues/<str:pk>/', revenue_detail_view, name='revenue'),
    path ('accounts/revenues/<str:pk>/update/', AccountsRevenueUpdate.as_view(), name='revenue_update'),
    path ('accounts/revenues/<str:pk>/delete/', AccountsRevenue_delete.as_view(), name='revenue_delete'),
    path ('accounts/revenues/create/', AccountsRevenueCreate.as_view(), name='revenue_create'),

    # accounts expenses 
    path ('accounts/expenses', AccountsExpenses.as_view(), name='expenses'),
    path ('accounts/expenses/<str:pk>', AccountsExpenseDetail.as_view(), name='expense'),
    path ('accounts/expenses/<str:pk>/update/', AccountsExpenseUpdate.as_view(), name='expense_update'),
    path ('accounts/expenses/<str:pk>/delete/', AccountsExpenseDelete.as_view(), name='expense_delete'),
    path ('accounts/expenses/create/', AccountsExpenseCreate.as_view(), name='expense_create'),
    
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)