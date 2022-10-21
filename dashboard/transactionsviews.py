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
    balance = 0
    
    for transaction in transactions:
        all_total_amount_paid_so_far+=int(transaction.amount_paid_or_paying)
        context = {
            'page_obj':page_obj,
            'transactions':transactions,
            'balance':balance,
            'all_total_amount_paid_so_far':all_total_amount_paid_so_far,
            }

        return render(request, 'dashboard/transactions/transactions.html',context)
# all_total_amount_paid_out_so_far+=int(out_transaction.amount_paid_or_paying)

    for in_transaction in in_transactions:
        all_total_amount_paid_so_far+=int(in_transaction.amount_paid_or_paying)
        context = {
            'page_obj':page_obj,
            'in_transactions':in_transactions,
            'balance':balance,
            'all_total_amount_paid_so_far':all_total_amount_paid_so_far,
            }

        return render(request, 'dashboard/transactions/transactions.html',context)
    
    for out_transaction in out_transactions:
        all_total_amount_paid_out_so_far+=int(out_transaction.amount_paid_or_paying)
        context = {
            'page_obj':page_obj,
            'out_transactions':out_transactions,
            'balance':balance,
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
    context = {'transactions': transactions}
    return render(request, 'dashboard/transactions/transaction_detail.html', context) 


class TransactionCreate(CreateView):
    template_name='dashboard/transactions/transaction_create.html'
    model= Transactions
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:transactions')
    form_class=TransactionCreateForm


class TransactionUpdate(SuccessMessageMixin,UserPassesTestMixin, UpdateView):
    template_name='dashboard/transactions/transaction_update.html'
    model= Transactions
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:transactions')
    success_message = "transaction Was updated Successfully"
    # form_class=TransactionCreateForm

    def test_func(self):
        transaction= self.get_object()

        if self.request.user.is_staff:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        transaction = self.get_object()
        self.fields = '__all__'
        return super().dispatch(request, *args, **kwargs)



class TransactionDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/transactions/transaction_delete.html'
    model= Transactions
    context_object_name = 'transaction'
    success_message = "transaction Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:transactions')