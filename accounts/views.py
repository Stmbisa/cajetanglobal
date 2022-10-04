import email
from email.message import EmailMessage
from django.shortcuts import render,redirect
from users.forms import RegisterUserCreationForm
from users.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login as Login_process, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



#This code will only be activated if they want activation
def registrationfunctionforactivation(request):
    first_name =request.POST.get('first_name')
    last_name =request.POST.get('last_name')
    phone =request.POST.get('phone')
    username =request.POST.get('username')
    country_of_orgin =request.POST.get('country_of_orgin')
    country_of_destination =request.POST.get('country_of_destination')
    nationality =request.POST.get('nationality')
    next_of_kin =request.POST.get('next_of_kin')
    next_of_kin_phone_number =request.POST.get('next_of_kin_phone_number')
    password =request.POST.get('password')
    password2 =request.POST.get('password2')
    if User.objects.filter(username=username).exists():
        messages.info(request, 'Email already used')
        return redirect('login')
    elif password != password2:
        messages.info(request, 'Passwords not matching')
        return redirect('register')
    else:
        user = User.objects.create(first_name=first_name, last_name=last_name, phone=phone, username=username\
            , country_of_orgin=country_of_orgin, country_of_destination=country_of_destination, nationality=nationality\
            , next_of_kin=next_of_kin, next_of_kin_phone_number=next_of_kin_phone_number, password=password,  )
        # return HttpResponseRedirect(reverse('blog:index_home'))
        
        #account activate
        current_site = get_current_site(request)
        mail_subject = 'Please activate your account'
        message = render_to_string('accounts/account_verification.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        # messages.success(request, 'Thank you, we have sent you a verification email on the email you provided')
        return redirect('/account/login/?command-verification&email='+email)



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congrats! Your account is now active')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('accounts:register')
    return #render(request, 'accounts/activate.html')


def register(request):
    if request.method == 'POST':
        form = RegisterUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully created an account')
            return redirect('blog:index_home')
            # first_name =form.cleaned_data['first_name']
            # last_name =form.cleaned_data['last_name']
            # phone =form.cleaned_data['phone']
            # username =form.cleaned_data['username']
            # country_of_orgin =form.cleaned_data['country_of_orgin']
            # country_of_destination =form.cleaned_data['country_of_destination']
            # nationality =form.cleaned_data['nationality']
            # next_of_kin =form.cleaned_data['next_of_kin']
            # next_of_kin_phone_number =form.cleaned_data['next_of_kin_phone_number']
            # password =form.cleaned_data['password1']

            # user = User.objects.create_user(first_name=first_name, last_name=last_name,phone=phone,username=username\
            #     , country_of_orgin=country_of_orgin, country_of_destination=country_of_destination, nationality=nationality\
            #         , next_of_kin=next_of_kin,  next_of_kin_phone_number=next_of_kin_phone_number,  password=password)
            # user.save()
    else:
        form = RegisterUserCreationForm
    context = {
        'form':form
        }
    return render(request, 'accounts/register.html', context)

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=email, password=password)

    if user is not None:
        auth.login(request, user)
        # messages.success(request, 'You are now logged in')
        return redirect('memberships:membership')

    else:
        messages.error(request, 'Invalid login credentials')
    return render(request, 'accounts/login.html')

login_required(login_url='accounts:login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Goodbye, logged out')
    return redirect('accounts:login')


def forgotPassword(request):
    email = request.POST.get('email')
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        #reset password
        current_site = get_current_site(request)
        mail_subject = 'Reset your Password'
        message = render_to_string('accounts/reset_password_email.html', {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        messages.success(request, 'Password ret has been sent to your email')
        return render(request, 'accounts/forgotPassword.html')

    else:
        messages.error(request, 'Account with this email does not exist')
        return render(request, 'accounts/forgotPassword.html')

    return render(request, 'accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user=None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.ssession['uid']= uid
        messages.success(request, 'Please reset your password')
        return redirect('accounts:resetpassword')
    else:
        messages.error(request, 'This link has expired')
        return redirect('accounts:login')


def resetpassword(request):
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    if password == confirm_password:
        uid = request.session.get('uid')
        user = User.objects.get(pk=uid)
        user.set_password(password)
        user.save()
        messages.success(request, 'Password reset successful')
        return redirect('accounts:login')

    else:
        messages.error(request, 'password do not match')
        return redirect('accounts:resetpassword')

    return render(request, 'accounts/resetpassword.html')

