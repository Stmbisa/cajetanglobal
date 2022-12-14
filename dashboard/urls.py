from django.urls import URLPattern, path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . views import *
       

from .expensesviews import *
            
from .transactionsviews import *

from .identityviews import *

from .datesviews import *
from .cashmemoviews import *
from .documentsviews import *
from .userviews import *
from .adminverifyuserviews import *
from .fileviews import *


app_name = "dashboard"
urlpatterns = [
    path ('', dashboard, name='dash_home'),
    path ('profiles/', profiles, name='profiles'),
    path ('profiles/search/', search_profile, name="search_profiles"),
    path ('profiles/<str:pk>', login_required(Profile_detail), name='profile'),
    path ('profiles/<str:pk>/update/', login_required(Profile_update.as_view()), name='profile_update'),
    path ('profiles/<str:pk>/delete/', login_required(Profile_delete.as_view()), name='profile_delete'),
    path ('profiles/create/', login_required(Profile_create.as_view()), name='profile_create'),


    #identities 
    path ('identities/', identities, name='identities'),

    # users
    path ('users/', users, name='users'),
    path ('users/search/', search_users, name="search_users"),
    path ('users/<str:pk>', UserDetail, name='user'),
    path ('users/<str:pk>/update/', login_required(UserUpdate.as_view()), name='user_update'),
    path ('users/<str:pk>/delete/', login_required(UserDelete.as_view()), name='user_delete'),
    path ('users/create/', login_required(UserCreate.as_view()), name='user_create'),
    
    #transactions 
    path ('transactions/', transactions, name='transactions'),
    path ('transactions/search/', search_transactions, name="search_transactions"),
    path ('transactions/<str:pk>', TransactionDetail, name='transaction'),
    path ('transactions/<str:pk>/update/', login_required(TransactionUpdate.as_view()), name='transaction_update'),
    path ('transactions/<str:pk>/delete/', login_required(TransactionDelete.as_view()), name='transaction_delete'),
    path ('transactions/create/', login_required(TransactionCreate.as_view()), name='transaction_create'),

    #dates 
    path ('eventsdates/', eventsdates, name='events'),
    path ('eventdates/search/', search_events, name="search_events"),
    path ('eventsdates/<str:pk>', EventDateDetail, name='event'),
    path ('eventsdates/<str:pk>/update/', login_required(EventDateUpdate.as_view()), name='event_update'),
    path ('eventsdates/<str:pk>/delete/', login_required(EventDateDelete.as_view()), name='event_delete'),
    path ('eventsdates/create/', login_required(EventDateCreate.as_view()), name='event_create'),

    

    # all accounts
    # path ('accounts/', Profiles.as_view(), name='accounts'),
    # accounts cashmemo 
   
    path ('cashmemos', cashmemos, name='cashmemos'),
    path ('cashmemos/<str:pk>/', CashmemoDetail, name='cashmemo'),
    path ('cashmemos/<str:pk>/update/', login_required(CashmemoUpdate.as_view()), name='cashmemo_update'),
    path ('cashmemos/<str:pk>/delete/', login_required(CashmemoDelete.as_view()), name='cashmemo_delete'),
    path ('cashmemos/create/add/', login_required(CashmemoCreate.as_view()), name='cashmemo_create'),


    # accounts expenses 
    path ('expenses', login_required(AccountsExpenses.as_view()), name='expenses'),
    path ('expenses/<str:pk>', AccountsExpenseDetail, name='expense'),
    path ('expenses/<str:pk>/update/', login_required(AccountsExpenseUpdate.as_view()), name='expense_update'),
    path ('expenses/<str:pk>/delete/', login_required(AccountsExpenseDelete.as_view()), name='expense_delete'),
    path ('expenses/create/', login_required(AccountsExpenseCreate.as_view()), name='expense_create'),

    #documents
    path ('documents/', documents, name='documents'),
    path ('documents/search/', search_documents, name="search_documents"),
    path ('documents/<str:pk>', DocumentDetail, name='document'),
    path ('documents/<str:pk>/update/', login_required(DocumentUpdate.as_view()), name='document_update'),
    path ('documents/<str:pk>/delete/', login_required(DocumentDelete.as_view()), name='document_delete'),
    path ('documents/create/', login_required(DocumentCreate.as_view()), name='document_create'),

    #documents
    path ('adminverify/', adminverifyusers, name='adminverifyusers'),
    path ('adminverify/<str:pk>', adminverifyUserDetail, name='adminverifyuserdetail'),
    path ('adminverify/search/', adminverifysearch, name="search_adminverify"),
    path ('adminverify/<str:pk>/update/', login_required(AdminverifyUserUpdate.as_view()), name='Adminverifyuserupdate'),


    #files 
    path ('files/', files, name='files'),
    path ('files/<str:pk>', file_detail, name='file_detail'),
    path ('files/search/', file_search, name="search_file"),

    
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)