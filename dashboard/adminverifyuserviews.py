from users.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator
from users.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render


@login_required
def adminverifyusers(request):
    users = User.objects.all()
    context = {
        'users':users,
        }

    return render(request, 'dashboard/adminverify/adminverify.html',context)
    
    


@login_required
def adminverifyUserDetail(request, pk):
    users = User.objects.filter(pk = pk)
    context = {'users': users}
    return render(request, 'dashboard/adminverify/adminverify_detail.html', context) 

# class AdminverifyUserUpdate(SuccessMessageMixin, UpdateView):
#     template_name='dashboard/adminverify/adminverify_update.html'
#     model= User
#     context_object_name = 'user'
#     success_message = "User Was updated Successfully"
#     success_url = reverse_lazy('dashboard:adminverifyusers')
#     fields = ('has_paid', 'has_done_biometry_before', 'has_done_biometry', 'has_obtained_visa_before',\
#          'rejected',)

class AdminverifyUserUpdate(SuccessMessageMixin, UpdateView):
    template_name='dashboard/adminverify/adminverify_update.html'
    model= User
    context_object_name = 'user'
    success_message = "User Was updated Successfully"
    success_url = reverse_lazy('dashboard:adminverifyusers')
    fields = ('has_paid', 'has_done_biometry_before', 'has_done_biometry', 'has_obtained_visa_before','rejected',)



# class AdminverifyUserUpdate(SuccessMessageMixin, UpdateView):
#     template_name='dashboard/adminverify/adminverify_update.html'
#     model= User
#     fields = ('has_paid', 'has_done_biometry_before', 'has_done_biometry', 'has_obtained_visa_before','rejected',)
#     success_url = reverse_lazy('dashboard:adminverifyusers')
#     success_message = "User Was updated Successfully"
#     # form_class=AdminUserUpdateform

#     def dispatch(self, request, *args, **kwargs):
#         transaction = self.get_object()
#         self.fields = '__all__'
#         return super().dispatch(request, *args, **kwargs)


def adminverifysearch(request):
    users = None 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            users = User.objects.order_by('id').filter(Q(first_name__icontains=keyword)| Q(last_name__icontains= keyword) |Q(country_of_destination__icontains= keyword)|Q(phone__icontains= keyword)) # fielter treats , as a and 
        context = {
            'users':users, 
        }
    return render(request, 'dashboard/adminverify/adminverify.html',context)