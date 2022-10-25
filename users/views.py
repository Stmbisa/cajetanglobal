from multiprocessing import context
from pyexpat import model
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login as Login_process, logout
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  DeleteView, CreateView, UpdateView
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from . models import Profile,User, Payment
from django.contrib.sites.shortcuts import get_current_site
from .forms import RegisterUserCreationForm

from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)




def login(request):
    return render(request, "users/login.html")






# requester views
# class RequesterSignUpView(CreateView):
#     model = User
#     form_class = RequesterSignUpForm
#     template_name = 'users/sign_up.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'requester'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         Login_process(self.request, user)
#         # return redirect('requester')
#         return redirect('blog:index_home')

def loginView(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=email, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        if user.is_admin or user.is_superuser:
            return redirect('dashboard:dash_home')
        elif user.is_provider:
            return redirect('users:provider')
        elif user.is_requester:
            return redirect('users:requester')
        else:
            return redirect('blog:index_home')
    else:
        messages.info(request, "Invalid email or Password")
        return render(request,'users/login.html')
        
@login_required
def logOut(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render (request, 'users/profile.html')

# def profiles(request):
#     user = User.objects.get(id = request.user.id)
#     queryset = Profile.objects.all()
#     context = {
#         'profile_list':queryset
#     }
    
#     return render(request, 'users/profiles.html')

#     user = User.objects.get(id = request.user.id)
#     queryset = Profile.objects.all()
#     context = {
#         'profile_list':queryset
#     }
    
#     return render(request, 'users/profiles.html')






@login_required
def profile_create_view(request, **kwargs):
    return render(request, 'users/profile.html', {'context': context})
    

    
        
@login_required
def profile_detail_view(request, id):
    # obj =Profile.objects.get(id=my_id)
    obj =get_object_or_404(Profile, id=id)
    context = {
        'object': obj
    }
    return render(request,'users/profile_detail.html', context)

@login_required
def profile_edit_view(request):
    obj =get_object_or_404(Profile, id=id)
    context = {
        'object': obj
    }
    return render(request,'users/profile_edit.html', context)

# @login_required
# def profile_delete_view(request, id):
#     obj =get_object_or_404(Profile, id=id)
#     if request.method=='POST':
#         obj.delete()
#         return redirect('../../')
#     context = {
#         'object': obj
#     }
#     return render(request, 'users/profile_delete.html', context )
class ListUserView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/admin/list_users.html'
    context_object_name = 'users'
    paginated_by = 10


    def get_queryset(self):
        return User.objects.order_by('-id')

class DeleteUserView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/admin/delete_user.html'
    success_url = reverse_lazy('dashboard:profiles')
    success_message = "User Was Deleted Successfully"

@login_required
def create_user_form(request):
    return render(request, 'users/admin/add_user.html')

@login_required
def create_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = make_password(password)
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email Already Exist')
            return redirect('dashboard:profile_create')
        elif User.objects.filter(username=username).exists():
            messages.warning(request,'Username Already Exist')
            return redirect('dashboard:profile_create')
        
        else:
            a = User(first_name=first_name, last_name=last_name, username=username, password=password, email=email, is_admin=True)
            a.save()
            messages.success(request, 'Admin Was Created Successfully')
            return redirect('dashboard:profiles')
    else:
        messages.error(request, 'Admin Was Not Created Successfully')
        return redirect('dashboard:profile_create')

def user_profile_view(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'user':user
    }
    return render(request, 'users/admin/user_profile_edit.html', context)

def user_profile_update(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        # email = request.POST('email')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        try:
            user = User.objects.get(id = request.user.id)
            user.avatar = avatar
            user.user_type = user_type
            user.first_name = first_name
            user.last_name = last_name
            user.gender = gender
            user.phone_number = phone_number
            user.birth_date = birth_date
            user.save()
            messages.success(request, 'Your profile updated successfully')
            redirect('dashboard:user_profile_view')
        except:
            messages.warning(request, 'Your profile not updated')
            redirect('dashboard:user_profile_update')
    return render(request, 'users/admin/user_profile_edit.html')

    
@login_required
def create_profile(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        # email = request.POST('email')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        current_user = request.user
        user_id = current_user.id
        print(user_id)

        Profile.objects.filter(id = user_id).create
        a = User(user_id=user_id, avatar=avatar, user_type=user_type,
        first_name=first_name, last_name=last_name, gender=gender, phone_number=phone_number,
        birth_date=birth_date)
        messages.success(request, 'Your Profile Was Created Successfully')
        return redirect('dashboard:user_profile')
    else:
        current_user = request.user
        user_id = current_user.id
        users = Profile.objects.filter(user_id = user_id)
        users = {'users': users}
        return render(request, 'users/admin/user_profile_create.html', users) 

def user_profile(request):
    current_user = request.user
    user_id = current_user.id
    users = Profile.objects.filter(user_id = user_id)
    users = {'users': users}
    return render(request, 'users/admin/user_profile.html', users)

