from django.shortcuts import render
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, 
                                       PasswordChangeForm)
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate,logout
from users.forms import RegisterUserCreationForm


def membership_view(request, *args, **kwargs):
    return render (request, "memberships/membership.html") 


def register(request):
    if request.method == 'POST':
        form = RegisterUserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            user =form.get_user()
            login(request, user)
            return redirect('memberships:membership')
        else:
            form = RegisterUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'memberships/register.html', context)
        
    else:
        form = RegisterUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'memberships/register.html', context)

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user =form.get_user()
            if user is not None and user.is_active:
                login(request, user)
                return redirect('memberships:membership')
        else:
            form = AuthenticationForm(request) 
            context ={"form":form }
            messages.info(request, "Invalid Username or Password")
            return render(request,'memberships/login.html', context)
        
    else:
        form = AuthenticationForm(request) 
        context ={"form":form }
        messages.info(request, "Invalid Username or Password")
        return render(request,'memberships/login.html', context)
    


    # if user is not None and user.is_active:
    #     login(request, user)
    #     return redirect('memberships:membership')
    

def logOut(request):
    logout(request)
    return redirect('memberships:login')