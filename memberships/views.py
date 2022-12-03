from django.shortcuts import render
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, 
                                       PasswordChangeForm)
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate,logout
from users.forms import RegisterUserCreationForm
from users.models import User, Profile
from users.forms import *
from django.contrib.auth.decorators import login_required


def membership_view(request, *args, **kwargs):
    return render (request, "memberships/membership.html") 

def profile(request):
    user = User.objects.get(id = request.user.id) 
    context ={
        'user':user
    }
    return render(request, 'memberships/profile.html')


# @login_required
# def userprofileupdate(request):
#     user = User.objects.get(id = request.user.id)
#     # if request.method == 'POST':
#     first_name = request.POST.get('first_name')
#     last_name = request.POST.get('last_name')
#     gender = request.POST.get('gender')
#     birth_date = request.POST.get('birth_date')
#     country_of_orgin = request.POST.get('country_of_orgin')
#     next_of_kin = request.POST.get('next_of_kin')
#     next_of_kin_phone = request.POST.get('birth_date')
#     country_of_destination = request.POST.get('country_of_destination')
#     currency_of_choice = request.POST.get('currency_of_choice')
#     nationality = request.POST.get('nationality')
#     avatar = request.FILES.get('avatar',False)
#     passport_document = request.FILES.get('avatar',False)
#     print(first_name,last_name,gender, birth_date, country_of_orgin,  )
        
#     try:
#         # user = User.objects.get(id = request.user.id)
#         Profile.objects.filter(id = request.user.id).create(user=user,first_name=first_name, last_name=last_name,gender=gender,\
#              birth_date=birth_date,country_of_orgin=country_of_orgin, next_of_kin=next_of_kin,next_of_kin_phone=next_of_kin_phone,\
#              country_of_destination=country_of_destination,currency_of_choice=currency_of_choice, nationality=nationality, \
#             avatar=avatar,passport_document=passport_document, )
#         # profile.first_name = first_name
#         # profile.last_name = last_name
#         # profile.gender = gender
#         # profile.birth_date = birth_date
#         # profile.country_of_orgin = country_of_orgin
#         # profile.next_of_kin = next_of_kin
#         # profile.next_of_kin_phone = next_of_kin_phone
#         # profile.country_of_destination = country_of_destination
#         # profile.currency_of_choice = currency_of_choice
#         # profile.nationality = nationality
#         # profile.avatar = avatar
#         # profile.passport_document = passport_document
#         # profile.save()
#         user.has_profile==True
#         messages.success(request, 'Profile successfully updated')
#         redirect('memberships:membership')

#     except:
#         messages.warning(request, 'Your profile failed to get updated')
#         redirect('./')
   
#     return render(request, 'memberships/userupdate.html' )


@login_required
def userprofileupdate(request):
    user = User.objects.get(id = request.user.id)
    if request.method == "POST":
        form = UserUpdateform(request.POST, instance=request.user)
        if form.is_valid():
            Profile.objects.filter(id = request.user.id).create
            form.save()
            messages.success(request, 'You successfully created a profile')
            return redirect('memberships:user_files_upload')
    else:
        form= UserUpdateform(instance=request.user)

    context = {
        'form':form
    }

    return render(request, 'memberships/userupdate.html' , context)


@login_required
def userfileupload(request):
    user = User.objects.get(id = request.user.id)
    if request.method == "POST":
        form = UserUpdateformFiles(request.POST, instance=request.user)
        if form.is_valid():
            Profile.objects.filter(id = request.user.id).create
            form.save()
            messages.success(request, 'You successfully created a profile')
            return redirect('memberships:profile')
    else:
        form= UserUpdateformFiles(instance=request.user)

    context = {
        'form':form
    }

    return render(request, 'memberships/userfileupload.html' , context)
    