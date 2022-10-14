from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from users.forms import ProfileCreateForm, AccountsRevenueForm, AccountsExpenseForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import User, Profile, AccountsRevenue, AccountsExpense
from datetime import datetime, timedelta
from email import message
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator



class AccountsRevenueCreate(CreateView):
    template_name='dashboard/accounts/revenue_create.html'
    model= AccountsRevenue
    success_url = reverse_lazy('dashboard:revenues')
    form_class=AccountsRevenueForm



class AccountsRevenues(ListView):
    template_name='dashboard/accounts/expenses.html'
    model= AccountsRevenue
    context_object_name = 'expenses'
    ordering = ['-day_on_which']

class AccountsRevenueDetail(DetailView):
    template_name='dashboard/accounts/expense_detail.html'
    model= AccountsRevenue
    # fields = '__all__'

def AccountsRevenueDetail(request, pk):
    transactions = AccountsRevenue.objects.filter(pk = pk)
    context = {'transactions': transactions}
    return render(request, 'dashboard/accounts/revenue_detail.html', context) 

class AccountsExpenseCreate(CreateView):
    template_name='dashboard/accounts/expense_create.html'
    model= AccountsRevenue
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:expenses')
    form_class=AccountsRevenueCreate



class AccountsRevenueUpdate(SuccessMessageMixin, UpdateView):
    template_name='dashboard/accounts/expense_update.html'
    model= AccountsRevenue
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:expenses')
    success_message = "Profile Was updated Successfully"
    form_class=AccountsRevenueCreate



class AccountsRevenue_delete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/accounts/expense_delete.html'
    model= AccountsRevenue
    context_object_name = 'AccountsExpense'
    success_message = "expense Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:expenses')


def revenue_add(request):
    if request.method == 'POST':
        form = AccountsRevenueForm(request.POST)
        if form.is_valid():
            form= form.cleaned_data['revenue_of']
            form= form.cleaned_data['name_of_the_cashmemo']
            form= form.cleaned_data['amount']
            form= form.cleaned_data['day_on_which']
            form= form.cleaned_data['evidence_document']
            form= form.cleaned_data['signature']

            form.save
            return redirect('dashboard:revenues')

        else:
            form = AccountsRevenueForm()
        
        return render(request, 'dashboard/accounts/revenue_create.html', {'form':form})





# expenses
class AccountsExpenses(ListView):
    template_name='dashboard/accounts/expenses.html'
    model= AccountsExpense
    context_object_name = 'expenses'
    ordering = ['-day_on_which']

class AccountsExpenseDetail(DetailView):
    template_name='dashboard/accounts/expense_detail.html'
    model= AccountsExpense
    # fields = '__all__'

def AccountsExpenseDetail(request, pk):
    transactions = AccountsExpense.objects.filter(pk = pk)
    context = {'transactions': transactions}
    return render(request, 'dashboard/accounts/expense_detail.html', context) 

class AccountsExpenseCreate(CreateView):
    template_name='dashboard/accounts/expense_create.html'
    model= AccountsExpense
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:expenses')
    form_class=AccountsExpenseForm



class AccountsExpenseUpdate(SuccessMessageMixin, UpdateView):
    template_name='dashboard/accounts/expense_update.html'
    model= AccountsExpense
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:expenses')
    success_message = "Profile Was updated Successfully"
    form_class=AccountsExpenseForm



class AccountsExpenseDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/accounts/expense_delete.html'
    model= AccountsExpense
    context_object_name = 'AccountsExpense'
    success_message = "expense Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:expenses')