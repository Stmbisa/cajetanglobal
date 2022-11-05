from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import ProfileCreateForm, AccountsExpenseForm, ProfileSearchform
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import *
from dashboard.models import *
from datetime import datetime, timedelta
from email import message
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    # startdate = datetime.today()
    # end_date = startdate + timedelta(days=30)

    # biometries = [prof for prof in Profile.objects if prof.is_due() ]
    all_users = User.objects.all().count()
    all_profiles = Profile.objects.all().count()
    all_paid_profiles = Profile.objects.filter(has_paid =True).count()
    all_rejected = Profile.objects.filter(rejected =True).count()
    # all_success = Profile.objects.filter(is_success =True).count()
    total_profile_revenues = 0
    total_revenues = 0
    total_expenses = 0
    all_revenue = Cashmemo.objects.all()
    for revenue in all_revenue:
        total_revenues+= revenue.amount
    
    all_expenses = AccountsExpense.objects.all()
    for expense in all_expenses:
        total_expenses+= expense.amount
    
    all_profiles_paid = Profile.objects.filter(has_paid =True)
    for profile_revenue in all_profiles_paid:
        total_profile_revenues+= profile_revenue.amount_paid_so_far
    
    total_revenues = int(total_revenues +total_profile_revenues)
    
    total_profits = int(total_revenues)-int(total_expenses)

    form = ProfileSearchform(request.POST or None)
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

    if request.method == 'POST':
        queryset = Profile.objects.filter(first_name__icontains=form['first_name'].value(),
                                    last_name__icontains=form['last_name'].value(),
                                    phonenumber__icontains=form['phonenumber'].value()
                                    )
        context = {
        "form": form,
        "queryset": queryset,
    }
                                    
    
    return render(request, 'dashboard/dashboard.html', context)


@login_required
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
        profile.save()
        user.has_profile==True
        messages.success(request, 'Profile successfully updated')
        redirect('memberships:membership')

    except:
        messages.warning(request, 'Your profile failed to get updated')
        redirect('./')
   
    return render(request, 'dashboard/userupdate.html' )


@login_required
def profiles(request):
    # user = User.objects.get(id = request.user.id)
    profiles = Profile.objects.all()
    # page_number = request.GET.get('page',1)
    paginator = Paginator(profiles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_total_amount_paid_so_far=0 
    all_total_amount_to_pay=0
    all_total_balance=0
    balance = 0
    
    for profile in profiles:
        balance = profile.amount_to_pay - profile.amount_paid_so_far #if profile.amount_paid_so_far and profile.amount_to_pay else balance==balance
        all_total_amount_paid_so_far+=profile.amount_paid_so_far
        all_total_amount_to_pay+=profile.amount_to_pay
        all_total_balance+=profile.balance
        context = {
            'page_obj':page_obj,
            'profiles':profiles,
            'balance':balance,
            'all_total_amount_paid_so_far':all_total_amount_paid_so_far,
            'all_total_amount_to_pay':all_total_amount_to_pay,
            'all_total_balance':all_total_balance
        }

        return render(request, 'dashboard/profiles.html',context)
    else:
        messages.success(request, 'Something isnt right')
        return render(request, 'dashboard/profiles.html')
#to change this in function based view






# class Profiles(ListView):
#     template_name='dashboard/profiles.html'
#     model= Profile
#     context_object_name = 'profiles'
#     ordering = ['-email']


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



# class AccountsRevenueCreate(CreateView):
#     template_name='dashboard/revenue_create.html'
#     model= AccountsRevenue
#     # fields = '__all__'
#     success_url = reverse_lazy('dashboard:revenues')
#     form_class=AccountsRevenueForm


























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