from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from users.forms import RegisterUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator
from users.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q 


@login_required
def users(request):
    users = User.objects.all()
    # all_transactions = User.transactions_set.all().order_by('Transaction_date')
    # all_documents = User.documents_set.all().order_by('date_submitted')
    # all_events = User.profileEvents_set.all().order_by('event_date')
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'users': users,
        'paginator':paginator,
        'page_obj':page_obj

        }


    return render(request, 'dashboard/users/users.html',context)
    
    


@login_required
def UserDetail(request, pk):
    users = User.objects.filter(pk = pk)
    context = {
        'users': users,

        }
   
    return render(request, 'dashboard/users/user_detail.html', context) 


class UserCreate(CreateView):
    template_name='dashboard/users/user_create.html'
    model= User
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:users')
    form_class=RegisterUserCreationForm


class UserUpdate(SuccessMessageMixin,UserPassesTestMixin, UpdateView):
    template_name='dashboard/users/user_update.html'
    model= User
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:users')
    success_message = "User Was updated Successfully"
    # form_class=TransactionCreateForm

    def test_func(self):
        transaction= self.get_object()

        if self.request.user.is_staff or self.request.user:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        transaction = self.get_object()
        self.fields = '__all__'
        return super().dispatch(request, *args, **kwargs)



class UserDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/users/user_delete.html'
    model= User
    context_object_name = 'user'
    success_message = "User Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:users')


def search_users(request):
    users = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            users = User.objects.order_by('id').filter(Q(first_name__icontains=keyword)| Q(last_name__icontains= keyword) |Q(country_of_destination__icontains= keyword)|Q(phone__icontains= keyword)) # fielter treats , as a and 
        context = {
            'users':users, 
        }
    return render(request, 'dashboard/users/users.html',context)


#  all_profiles = Profile.objects.all().count()
#     all_paid_profiles = Profile.objects.filter(has_paid =True).count()