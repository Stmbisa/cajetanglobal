from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from datetime import datetime, timedelta
from email import message
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required
def documents(request):
    documents = Documents.objects.all()
    paginator = Paginator(documents, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'documents':documents,
        }

    return render(request, 'dashboard/documents/documents.html',context)

    
    


# all list of documents by this profile will be rendered by this view 


@login_required
def DocumentDetail(request, pk):
    transactions = Transactions.objects.filter(pk = pk)
    context = {'transactions': transactions}
    return render(request, 'dashboard/transactions/document_detail.html', context) 


class DocumentCreate(CreateView):
    template_name='dashboard/documents/document_create.html'
    model= Transactions
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:documents')
    form_class=DocumentSubmitForm


class DocumentUpdate(SuccessMessageMixin,UserPassesTestMixin, UpdateView):
    template_name='dashboard/documents/document_update.html'
    model= Documents
    success_url = reverse_lazy('dashboard:documents')
    success_message = "document Was updated Successfully"
    form_class=DocumentSubmitForm
    fields = '__all__'

    # def test_func(self):
    #     document= self.get_object()

    #     if self.request.user.is_staff:
    #         return True
    #     return False

    # def dispatch(self, request, *args, **kwargs):
    #     document = self.get_object()
    #     self.fields = '__all__'
    #     return super().dispatch(request, *args, **kwargs)



class DocumentDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/documents/document_delete.html'
    model= Documents
    context_object_name = 'document'
    success_message = "document Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:documents')