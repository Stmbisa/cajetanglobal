from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from dashboard.models import Cashmemo
from datetime import datetime, timedelta
from email import message
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def cashmemos(request):
    cashmemos = Cashmemo.objects.all()
    paginator = Paginator(cashmemos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_cash_in=0 
    balance = 0
    
    for cashmemo in cashmemos:
        all_cash_in+=int(cashmemo.amount)
        context = {
            'page_obj':page_obj,
            'cashmemos':cashmemos,
            'balance':balance,
            'all_cash_in':all_cash_in,
            }
        return render(request, 'dashboard/cashmemos/cashmemos.html',context)

    else:
        messages.warning(request, 'Something isnt right')
        return render(request, 'dashboard/cashmemos/cashmemos.html')
    
    


# all list of cashmemos by this profile will be rendered by this view 


@login_required
def CashmemoDetail(request, pk):
    cashmemos = Cashmemo.objects.filter(pk = pk)
    context = {'Cashmemos': cashmemos}
    return render(request, 'dashboard/cashmemos/transaction_detail.html', context) 


class CashmemoCreate(CreateView):
    template_name='dashboard/cashmemos/Cashmemo_create.html'
    model= Cashmemo
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:cashmemos')
    form_class=CashmemoCreateForm


class CashmemoUpdate(SuccessMessageMixin,UserPassesTestMixin, UpdateView):
    template_name='dashboard/cashmemos/transaction_update.html'
    model= Cashmemo
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:cashmemos')
    success_message = "Cashmemo Was updated Successfully"
    # form_class=CashmemoCreateForm

    def test_func(self):
        cashmemo= self.get_object()

        if self.request.user.is_staff:
            return True
        return False

    def dispatch(self, request, *args, **kwargs):
        cashmemo = self.get_object()
        self.fields = '__all__'
        return super().dispatch(request, *args, **kwargs)



class CashmemoDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/cashmemos/cashmemo_delete.html'
    model= Cashmemo
    context_object_name = 'Cashmemo'
    success_message = "Cashmemo Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:cashmemos')

