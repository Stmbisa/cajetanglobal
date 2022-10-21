from urllib import request
from .models import *

from django.contrib import admin
from .forms import *

class TransactionCreateAdmin(admin.ModelAdmin):
    list_display  = ['profile', 'Transaction_date', 'amount_paid_or_paying','reason', ]
    form = TransactionCreateForm
    list_filter =  ['profile']
    search_fields =['profile', 'Transaction_date','reason',]

class ProfileEventsCreateFormAdmin(admin.ModelAdmin):
    list_display  = ['profile','event_name', 'event_date']
    form = ProfileEventsCreateForm
    list_filter =  ['profile','event_name', 'event_date']
    search_fields = ['profile','event_name', 'event_date']


class DocumentSubmitFormAdmin(admin.ModelAdmin):
    list_display  = ['document_name','document_owner', 'date_submitted']
    form = DocumentSubmitForm
    list_filter =  ['document_name','document_owner', 'date_submitted']
    search_fields = ['document_name','document_name', 'document_name']



admin.site.register(Transactions, TransactionCreateAdmin)
admin.site.register(ProfileEvents, ProfileEventsCreateFormAdmin)
admin.site.register(Documents, DocumentSubmitFormAdmin)
