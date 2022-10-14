from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .forms import TransactionCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import User, Profile
from datetime import datetime, timedelta
from email import message
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView, CreateView
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Transactions
from .forms import *

def eventsdates(request):
    events = ProfileEvents.objects.all()
    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'events':events,
        }

    return render(request, 'dashboard/dates/dates.html', context)
    # else:
    #     messages.success(request, 'Something isnt right')
    #     return render(request, 'dashboard/dates/dates.html')


# all list of transactions by this profile will be rendered by this view 
def EventDateDetail(request, pk):
    event = ProfileEvents.objects.get(pk=pk)
    profile = Profile.objects.get(pk = pk)
    events_profile = profile.profileEvents_set.all()
    paginator = Paginator(events_profile, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'event':event,
        'page_obj':page_obj,
        'events':events_profile,
        }

    return render(request, 'dashboard/dates/dates.html', context)

# class EventDateDetail(DetailView):
#     template_name='dashboard/dates/eventdate_detail.html'
#     model= ProfileEvents
#     fields = '__all__'


class EventDateCreate(CreateView):
    template_name='dashboard/dates/eventdate_create.html'
    model= ProfileEvents
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:eventsdates')
    form_class=ProfileEventsCreateForm


class EventDateUpdate(SuccessMessageMixin,UserPassesTestMixin, UpdateView):
    template_name='dashboard/dates/eventdate_update.html'
    model= ProfileEvents
    # fields = '__all__'
    success_url = reverse_lazy('dashboard:eventsdates')
    success_message = "eventdate Was updated Successfully"
    # form_class=ProfileEventsCreateForm


class EventDateDelete(SuccessMessageMixin, DeleteView):
    template_name='dashboard/dates/eventdate_delete.html'
    model= ProfileEvents
    context_object_name = 'eventdate'
    success_message = "eventdate Was Deleted Successfully"
    success_url = reverse_lazy('dashboard:eventsdates')