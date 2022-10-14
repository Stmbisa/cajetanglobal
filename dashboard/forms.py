from django import forms
from .models import *
import datetime

class DateInput(forms.DateInput):
    input_type: 'date'


class TransactionCreateForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'

class TransactionSearchForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['profile', 'Transaction_date']
        widgets = {
            'Transaction_date': DateInput(attrs={'type':'date'}),}

class ProfileEventsCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileEvents
        fields = '__all__'