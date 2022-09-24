from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Profile, Announcement, Accounts_revenue, Accounts_expense

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

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

class AnnouncementCreateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

class RegisterUserCreationForm(UserCreationForm):
    class Meta:
        model =User
        fields = '__all__'
        fields = ('first_name', 'last_name','gender', 'phone','username', 'country_of_orgin','country_of_destination', 
        'nationality', 'next_of_kin','next_of_kin_phone_number', 'has_taken_biometry_before',)


class Accounts_revenueForm(forms.ModelForm):
    class Meta:
        model = Accounts_revenue
        fields = '__all__'

class Accounts_expenseForm(forms.ModelForm):
    class Meta:
        model = Accounts_expense
        fields = '__all__'