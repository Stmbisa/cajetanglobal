from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Profile, Announcement, AccountsExpense
import datetime

class DateInput(forms.DateInput):
    input_type: 'date'

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'biometry_date': DateInput(attrs={'type':'date'}),
            'Departure_date': DateInput(attrs={'type':'date'}),
            'birth_date': DateInput(attrs={'type':'date'}),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('user', css_class='form-group col-md-3 mb-0'),
                Column('avatar', css_class='form-group col-md-3 mb-0'),
                Column(' has_passport', css_class='form-group col-md-3 mb-0'),
                Column('passport_document', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='form-group col-md-4 mb-0'),
                Column('phonenumber', css_class='form-group col-md-4 mb-0'),
                Column('birth_date', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('next_of_kin', css_class='form-group col-md-4 mb-0'),
                Column('next_of_kin_phone', css_class='form-group col-md-4 mb-0'),
                Column('country_of_orgin', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'amount_paid_so_far',
            'amount_paid_today',
            'amount_to_pay',
            'balance',
            'brought_by',
            Row(
                Column('currency_of_choice', css_class='form-group col-md-4 mb-0'),
                Column('country_of_destination', css_class='form-group col-md-4 mb-0'),
                Column('nationality', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'has_paid',
            'biometry_date',
            'has_done_biometry',
            Row(
                Column('has_done_biometry_before', css_class='form-group col-md-3 mb-0'),
                Column('has_obtained_visa_before', css_class='form-group col-md-3 mb-0'),
                Column('has_obtained_visa', css_class='form-group col-md-3 mb-0'),
                Column('rejected', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'Departure_date',
            Submit('submit', 'Sign in')
        )

class ProfileUserUpdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['passport_document','first_name', 'last_name','gender','email', 'phonenumber', 'birth_date', 'next_of_kin',\
                  'next_of_kin_phone', 'country_of_orgin', 'country_of_destination', 'nationality']
        widgets = {
            'birth_date': DateInput(attrs={'type':'date'}),        
        }

class UserUpdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['has_done_biometry_before','has_obtained_visa_before',]

class AdminUserUpdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['has_done_biometry_before','has_obtained_visa_before','is_verified','has_paid','has_done_biometry','has_obtained_visa','rejected']

class UserUpdateformFiles(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar','passport_document','covid_certificate','yellow_fever']




class AnnouncementCreateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

class RegisterUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm Password",
        "class":"form_control"
    })),
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm Password",
         "class":"form_control"
    }))

    class Meta:
        model =User
        # fields = '__all__'
        fields = ('first_name', 'last_name','gender', 'phone','username', 'country_of_orgin','country_of_destination', 
        'nationality', 'next_of_kin','next_of_kin_phone_number', 'has_taken_biometry_before',)
        def __init__(self, *args, **kwargs):
            super(RegisterUserCreationForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder']='Type your First Name'
            self.fields['Last_name'].widget.attrs['placeholder']='Type your Last Name'
            self.fields['phone'].widget.attrs['placeholder']='Type your number'
            self.fields['username'].widget.attrs['placeholder']='Type your email'
            self.fields['country_of_orgin'].widget.attrs['placeholder']='Your country of origin'
            self.fields['country_of_destination'].widget.attrs['placeholder']='Where do you want to go'
            self.fields['nationality'].widget.attrs['placeholder']='Your nationality'
            self.fields['next_of_kin'].widget.attrs['placeholder']='Whom can we call if you are not available'
            self.fields['next_of_kin_phone_number'].widget.attrs['placeholder']='Whats their number '
            for field in self.fields:
                self.fields[field].widget.attrs['class']='form-control'


class AccountsExpenseForm(forms.ModelForm):
    class Meta:
        model = AccountsExpense
        fields = '__all__'

class AccountsExpenseSearch(forms.ModelForm):
    class Meta:
        model = AccountsExpense
        fields = ['expense_of', 'expense_by',]