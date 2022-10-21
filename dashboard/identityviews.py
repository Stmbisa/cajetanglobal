
from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required
def identities(request):
    # user = User.objects.get(id = request.user.id)
    profiles = Profile.objects.all()
    # page_number = request.GET.get('page',1)
    paginator = Paginator(profiles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    for profile in profiles:
        balance = profile.amount_to_pay - profile.amount_paid_so_far #if profile.amount_paid_so_far and profile.amount_to_pay else balance==balance
        context = {
            'page_obj':page_obj,
            'profiles':profiles,
        }

        return render(request, 'dashboard/identities/identities.html',context)
    else:
        messages.success(request, 'Something isnt right')
        return render(request, 'dashboard/identities/identities.html')
#to change this in function based view




