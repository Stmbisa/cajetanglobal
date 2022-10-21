from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from users.forms import ProfileCreateForm, AccountsExpenseForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import *
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


@login_required
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