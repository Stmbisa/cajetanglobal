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


@login_required
def users(request):
    users = User.objects.all()
    context = {
        'users':users,
        }

    return render(request, 'dashboard/users/users.html',context)
    
    


@login_required
def UserDetail(request, pk):
    users = User.objects.filter(pk = pk)
    context = {'users': users}
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
    success_url = reverse_lazy('dashboard:transactions')
    success_message = "User Was updated Successfully"
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



class UserDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/users/user_delete.html'
    model= User
    context_object_name = 'user'
    success_message = "User Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:users')