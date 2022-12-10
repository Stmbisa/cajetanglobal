from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Transactions
from django.contrib.auth.decorators import login_required
from django.db.models import Q 


@login_required
def transactions(request):
    transactions = Transactions.objects.all()
    in_transactions = Transactions.objects.filter(status='in')
    out_transactions = Transactions.objects.filter(status='out')
    paginator = Paginator(transactions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_total_amount_paid_so_far=0 
    all_total_amount_paid_out_so_far=0 
   
    
    for transaction in transactions:
        all_total_amount_paid_so_far+=int(transaction.amount_paid_or_paying)
        balance = int(transaction.amount_to_pay) - int(transaction.amount_paid_or_paying)
        context = {
            'page_obj':page_obj,
            'transactions':transactions,
            'all_total_amount_paid_so_far':all_total_amount_paid_so_far,
            'balance':balance,
            }

        return render(request, 'dashboard/transactions/transactions.html',context)
# all_total_amount_paid_out_so_far+=int(out_transaction.amount_paid_or_paying)

    for in_transaction in in_transactions:
        all_total_amount_paid_so_far+=int(in_transaction.amount_paid_or_paying)
        context = {
            'page_obj':page_obj,
            'in_transactions':in_transactions,
            'all_total_amount_paid_so_far':all_total_amount_paid_so_far,
            }

        return render(request, 'dashboard/transactions/transactions.html',context)
    
    for out_transaction in out_transactions:
        all_total_amount_paid_out_so_far+=int(out_transaction.amount_paid_or_paying)
        context = {
            'page_obj':page_obj,
            'out_transactions':out_transactions,
            'all_total_amount_paid_so_far':all_total_amount_paid_so_far,
            }

        return render(request, 'dashboard/transactions/transactions.html',context)

    else:
        messages.warning(request, 'Something isnt right')
        return render(request, 'dashboard/transactions/transactions.html')
    
    


# all list of transactions by this profile will be rendered by this view 
# class TransactionDetail(DetailView):
#     template_name='dashboard/transactions/transaction_detail.html'
#     model= Transactions
#     fields = '__all__'

@login_required
def TransactionDetail(request, pk):
    transactions = Transactions.objects.filter(pk = pk)
    # balance = int(transactions.amount_to_pay)-int(transactions.amount_paid_or_paying)
    context = {
        'transactions': transactions,
        # 'balance': balance
        }
    return render(request, 'dashboard/transactions/transaction_detail.html', context) 


class TransactionCreate(CreateView):
    template_name='dashboard/transactions/transaction_create.html'
    model= Transactions
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:transactions')
    form_class=TransactionCreateForm


# def TransactionUpdate(request, pk):
 
#     obj = get_object_or_404(Transactions, pk = pk)
 
#     form = TransactionCreateForm(request.POST or None, instance = obj)

#     if form.is_valid():
#         form.save()
#         return redirect ('dashboard:transactions', pk=pk)
    
#     context ={
#         "form" : form,
#         "obj" : obj
#     }
 
#     return render(request, "dashboard/transactions/transaction_update.html", context)

class TransactionUpdate(SuccessMessageMixin, UpdateView):
    template_name='dashboard/transactions/transaction_update.html'
    model= Transactions
    context_object_name = 'transaction'
    success_message = "transaction Was updated Successfully"
    success_url = reverse_lazy('dashboard:transactions')
    fields = ('profile', 'Transaction_date', 'amount_paid_or_paying', 'amount_to_pay', 'status', 'reason')






class TransactionDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/transactions/transaction_delete.html'
    model= Transactions
    context_object_name = 'transaction'
    success_message = "transaction Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:transactions')


def search_transactions(request):
    transactions = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            transactions = Transactions.objects.order_by('id').filter(Q(profile__first_name__icontains=keyword)| Q(profile__last_name__icontains= keyword)| Q(Transaction_date__icontains= keyword)|Q(profile__country_of_destination__icontains= keyword)|Q(profile__phone__icontains= keyword)|Q(reason__icontains= keyword)) # fielter treats , as a and 
        context = {
            'transactions':transactions, 
        }
    return render(request, 'dashboard/transactions/transactions.html',context)