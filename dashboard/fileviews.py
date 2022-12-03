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
def files(request):
    # user = User.objects.get(id = request.user.id)
    files = User.objects.all()
    # page_number = request.GET.get('page',1)
    paginator = Paginator(files, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "files": files,
        "paginator": paginator,
        "page_number": page_number,
        "page_obj": page_obj,
    }
    return render(request, 'dashboard/files/files.html', context)
#to change this in function based view




def file_detail(request, pk):
    users = User.objects.filter(pk = pk)
    context = {'users': users}
    return render(request, 'dashboard/files/profile_detail.html', context) 

def file_search(request):
    files = None 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            files = User.objects.order_by('id').filter(Q(first_name__icontains=keyword)| Q(last_name__icontains= keyword) |Q(country_of_destination__icontains= keyword)|Q(phone__icontains= keyword)) # fielter treats , as a and 
        context = {
            'files':files, 
        }
    return render(request, 'dashboard/files/files.html',context)