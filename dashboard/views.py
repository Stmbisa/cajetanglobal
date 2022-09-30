from multiprocessing import context
import profile
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms import ProfileCreateForm, Accounts_revenueForm, Accounts_expenseForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import User, Profile, Accounts_revenue, Accounts_expense
from datetime import datetime, timedelta
from email import message
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def dashboard(request):
    # startdate = datetime.today()
    # end_date = startdate + timedelta(days=30)

    # biometries = [prof for prof in Profile.objects if prof.is_due() ]
    all_users = User.objects.all().count()
    all_profiles = Profile.objects.all().count()
    all_paid_profiles = Profile.objects.filter(has_paid =True).count()
    all_rejected = Profile.objects.filter(rejected =True).count()
    total_profile_revenues = 0
    total_revenues = 0
    total_expenses = 0
    all_revenue = Accounts_revenue.objects.all()
    for revenue in all_revenue:
        total_revenues+= revenue.amount
    
    all_expenses = Accounts_expense.objects.all()
    for expense in all_expenses:
        total_expenses+= expense.amount
    
    all_profiles_paid = Profile.objects.filter(has_paid =True)
    for profile_revenue in all_profiles_paid:
        total_profile_revenues+= profile_revenue.amount_paid_so_far
    
    total_revenues = total_revenues +total_profile_revenues
    
    total_profits = total_revenues-total_expenses
    context ={
        # 'biometries': biometries,
        'all_users': all_users,
        'all_profiles': all_profiles,
        'all_paid_profiles': all_paid_profiles,
        'all_rejected': all_rejected,
        'total_revenues': total_revenues,
        'total_expenses': total_expenses,
        'total_profits': total_profits,
    }
    return render(request, 'dashboard/dashboard.html', context)

def userprofileupdate(request):
    # user = User.objects.get(id = request.user.id)
    # if request.method == 'POST':
    avatar = request.FILES.get('avatar',False)
    passport_document = request.FILES.get('avatar',False)
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    gender = request.POST.get('gender')
    birth_date = request.POST.get('birth_date')
    country_of_orgin = request.POST.get('country_of_orgin')
    next_of_kin = request.POST.get('next_of_kin')
    next_of_kin_phone = request.POST.get('birth_date')
    country_of_destination = request.POST.get('country_of_destination')
    currency_of_choice = request.POST.get('currency_of_choice')
    nationality = request.POST.get('nationality')
    password = request.POST.get('password')
        
    try:
        user = User.objects.get(id = request.user.id)
        profile = Profile.objects.filter(id = request.user.id)
        profile.avatar = avatar
        profile.passport_document = passport_document
        profile.first_name = first_name
        profile.last_name = last_name
        profile.gender = gender
        profile.birth_date = birth_date
        profile.country_of_orgin = country_of_orgin
        profile.next_of_kin = next_of_kin
        profile.next_of_kin_phone = next_of_kin_phone
        profile.country_of_destination = country_of_destination
        profile.currency_of_choice = currency_of_choice
        profile.nationality = nationality
        password.replace(" ", '')
        if password != None and password !='':
            user.set_password(password)
        # profile.save()
        messages.success(request, 'Profile successfully updated')
        redirect('memberships:membership')

    except:
        messages.warning(request, 'Your profile failed to get updated')
        redirect('./')
   
    return render(request, 'dashboard/userupdate.html' )


class Profiles(ListView):
    template_name='dashboard/profiles.html'
    model= Profile
    context_object_name = 'profiles'
    ordering = ['-email']


class Profile_detail(DetailView):
    template_name='dashboard/profile_detail.html'
    model= Profile
    fields = '__all__'

class Profile_create(CreateView):
    template_name='dashboard/profile_create.html'
    model= Profile
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:profiles')
    form_class=ProfileCreateForm


class Profile_update(SuccessMessageMixin,UserPassesTestMixin, UpdateView):
    template_name='dashboard/profile_update.html'
    model= Profile
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:profiles')
    success_message = "Profile Was updated Successfully"
    # form_class=ProfileCreateForm

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(self.form_class)
    #     if not self.request.user.is_staff:
    #         form.fields.pop('amount_to_pay')
    #     return form

    def test_func(self):
        profile= self.get_object()

        if self.request.user==profile.user or self.request.user.is_staff:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        profile = self.get_object()
        self.fields = '__all__'
        if request.user.is_superuser:
            self.fields = '__all__'
        else:
            self.fields = ('avatar','has_passport','passport_document', 'first_name', 'last_name',
            'gender', 'phonenumber','username', 'country_of_orgin','country_of_destination', 'currency_of_choice',
        'nationality', 'next_of_kin','next_of_kin_phone_number', 'has_taken_biometry_before',)
        return super().dispatch(request, *args, **kwargs)


class Profile_delete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/profile_delete.html'
    model= Profile
    context_object_name = 'profile'
    success_message = "Profile Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:profiles')


#accounts 
class Accounts_revenues(ListView):
    template_name='dashboard/revenues.html'
    model= Accounts_revenue
    context_object_name = 'revenues'
    ordering = ['-day_on_which']


class Accounts_revenue_detail(DetailView):
    template_name='dashboard/revenue_detail.html'
    model= Accounts_revenue
    fields = '__all__'

class Accounts_revenue_create(CreateView):
    template_name='dashboard/revenue_create.html'
    model= Profile
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:revenues')
    form_class=Accounts_revenueForm


class Accounts_revenue_update(SuccessMessageMixin, UpdateView):
    template_name='dashboard/revenue_update.html'
    model= Profile
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:revenues')
    success_message = "Profile Was updated Successfully"
    form_class=Accounts_revenueForm


class Accounts_revenue_delete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/revenue_delete.html'
    model= Accounts_revenue
    context_object_name = 'accounts_revenue'
    success_message = "Revenue Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:revenues')



# expenses
class Accounts_expenses(ListView):
    template_name='dashboard/expenses.html'
    model= Accounts_expense
    context_object_name = 'expenses'
    ordering = ['-day_on_which']


class Accounts_expense_detail(DetailView):
    template_name='dashboard/expense_detail.html'
    model= Accounts_expense
    fields = '__all__'

class Accounts_expense_create(CreateView):
    template_name='dashboard/expense_create.html'
    model= Accounts_expense
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:expenses')
    form_class=Accounts_expenseForm


class Accounts_expense_update(SuccessMessageMixin, UpdateView):
    template_name='dashboard/expense_update.html'
    model= Accounts_expense
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:expenses')
    success_message = "Profile Was updated Successfully"
    form_class=Accounts_expenseForm


class Accounts_expense_delete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/expense_delete.html'
    model= Accounts_expense
    context_object_name = 'accounts_expense'
    success_message = "expense Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:expenses')



# def profiles(request):
#     # user = User.objects.get(id = request.user.id)
#     queryset = Profile.objects.all()
#     context = {
#         'profile_list':queryset
#     }
    
#     return render(request, 'dashboard/profiles.html',context)

# def add_profile(request):
#     form=ProfileCreateForm(request.POST)
#     if form.is_valid():
#         form.save()
#         # fullname = form.cleaned_data.get('username')
#         fullname = Profile.full_name
#         messages.success(request, f'Account created for {fullname}')
#         return redirect('dashboard:profiles')
#     else:
#         form = ProfileCreateForm()
#         context = {
#             'form': form
#         }
#     context ={"form":form}
#     return render(request, 'dashboard/profile_add.html',context)