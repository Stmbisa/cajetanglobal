from django import forms
from .models import *
import datetime

class DateInput(forms.DateInput):
    input_type: 'date'


class TransactionCreateForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'
        widgets = {
            'Transaction_date': DateInput(attrs={'type':'date'}),}

class TransactionSearchForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['profile', 'Transaction_date']
        

class ProfileEventsCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileEvents
        fields = '__all__'
        widgets = {
            'event_date': DateInput(attrs={'type':'date'}),}


class CashmemoCreateForm(forms.ModelForm):
    class Meta:
        model = Cashmemo
        fields = '__all__'

class CashmemoSearch(forms.ModelForm):
    class Meta:
        model = Cashmemo
        fields = [ 'cashmemo_by',]

class DocumentSubmitForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = '__all__'

class DocumentSearchForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = [ 'document_owner','document_name']