from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from users.models import *
from dashboard.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q 


@login_required
def dashboard(request):
    # startdate = datetime.today()
    # end_date = startdate + timedelta(days=30)

    # biometries = [prof for prof in Profile.objects if prof.is_due() ]
    all_users = User.objects.all().count()
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

    context ={
        # 'biometries': biometries,
        'all_users': all_users,
        'all_rejected': all_rejected,
        'total_revenues': total_revenues,
        'total_expenses': total_expenses,
        'total_profits': total_profits,
    }
                                    
    
    return render(request, 'dashboard/dashboard.html', context)



@login_required
def profiles(request):
    # user = User.objects.get(id = request.user.id)
    profiles = User.objects.all()
    # page_number = request.GET.get('page',1)
    paginator = Paginator(profiles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "profiles": profiles,
        "paginator": paginator,
        "page_number": page_number,
        "page_obj": page_obj,
    }
    return render(request, 'dashboard/profiles.html', context)
#to change this in function based view






# class Profiles(ListView):
#     template_name='dashboard/profiles.html'
#     model= Profile
#     context_object_name = 'profiles'
#     ordering = ['-email']



def Profile_detail(request, pk):
    users = User.objects.filter(pk = pk)
    context = {'users': users}
    return render(request, 'dashboard/profile_detail.html', context) 

class Profile_create(CreateView):
    template_name='dashboard/profile_create.html'
    model= User
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:profiles')
    form_class=RegisterUserCreationForm

class Profile_update(SuccessMessageMixin, UpdateView):
    template_name='dashboard/profile_update.html'
    model= User
    context_object_name = 'profile'
    success_message = "Profile Was updated Successfully"
    success_url = reverse_lazy('dashboard:profiles')
    fields = ('first_name', 'last_name', 'gender', 'phone', 'birth_date', 'country_of_orgin', 'country_of_destination', \
        'nationality', 'next_of_kin', 'next_of_kin_phone_number', 'has_paid', 'has_done_biometry_before', 'has_done_biometry', 'has_obtained_visa_before',\
         'rejected', 'passport_document', 'covid_certificate', 'yellow_fever')



class Profile_delete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/profile_delete.html'
    model= User
    context_object_name = 'profile'
    success_message = "Profile Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:profiles')

def search_profile(request):
    profiles = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            profiles = User.objects.order_by('id').filter(Q(first_name__icontains=keyword)| Q(last_name__icontains= keyword) |Q(country_of_destination__icontains= keyword)|Q(phone__icontains= keyword)) # fielter treats , as a and 
    context = {
        'profiles':profiles, 
    }
    return render(request, 'dashboard/profiles.html',context )


























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