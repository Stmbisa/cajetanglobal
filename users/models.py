from locale import currency
from time import timezone
from django.urls import reverse
from email.policy import default
from typing_extensions import Required
from django.db import models
from datetime import datetime, timedelta
from datetime import *
from django.utils import timezone
# import dataclasses
from django.contrib.auth.models import AbstractUser
from django.db import models

import os
from .manager import UserManager

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)



class User(AbstractUser):
    is_verified= models.BooleanField(default=False) 
    is_active= models.BooleanField(default=True)
    has_taken_biometry_before= models.BooleanField(default=False, help_text='Tick if you have ever taken the biometry')
    avatar = models.ImageField(upload_to = 'uploads/', default='')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
       ]
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES,null=False,default='', blank=False)
    username=models.EmailField(unique=True, null=True, help_text='Type in your email, Required. Letters, numbers and @/./+/-/_ characters')
    phone = models.CharField(max_length=14, default='', unique=True, null=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password=models.CharField(max_length=100, null=True, blank=True)
    last_login = models.DateField(auto_now=True, null=True, blank=True)
    last_logout = models.DateField(auto_now=True, null=True, blank=True)
    country_of_orgin = models.CharField(max_length=100, null=False, blank=False, default='')
  

    COUNTRY_CHOICES = [
        ("Australia", 'Australia'),
        ("Canada", 'Canada'),
        ("USA", 'USA'),
        ("Shengen", 'Shengen'),
        ("Israel", 'Israel'),

       ]
    country_of_destination = models.CharField(max_length=100,choices=COUNTRY_CHOICES,default='US', null=False, blank=False)
    nationality = models.CharField(max_length=100, null=False, blank=False, default='')
    next_of_kin = models.CharField(max_length=255, default='', help_text='whom would we call if you are not available')
    next_of_kin_phone_number = models.CharField(max_length=14, default='')
    
    
    objects: UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name','phone']

    def __str__(self):
        return self.username or ''
        # return self.first_name+ ' ' + str(self.last_name)
    @property
    def full_name(self):
        "returns User's fullname"
        return '%s %s'%(self.first_name,self.last_name)

    def get_image(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/assets/img/user.png"

class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_paid = models.BooleanField(default=False)
    amount_paid=models.CharField(max_length=100, default='')
    paid_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.content)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True )
    avatar = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    has_passport = models.BooleanField(default=True)
    passport_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    first_name = models.CharField(max_length=255, default='',null=True, blank=True)
    last_name = models.CharField(max_length=255, default='',null=True, blank=True)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
       ]

    
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='',null=True)
    email = models.EmailField(default='',blank=True, null=True)
    phonenumber = models.CharField(max_length=15,null=True,blank=True, default='') #blank=True, null=True
    birth_date = models.DateField(blank=True, default='', null=True,help_text='')
    next_of_kin = models.CharField(max_length=255, default='', null=True, blank=True)
    next_of_kin_phone = models.IntegerField(unique=True, null=True, blank=True)
    country_of_orgin = models.CharField(max_length=255, default='', null=True, blank=True)
    amount_paid_so_far= models.DecimalField(max_length=255, null=True,blank=True, default=0, decimal_places=3, max_digits=15)
    amount_paid_today= models.DecimalField(max_length=255, null=True,blank=True, default=0, decimal_places=3, max_digits=15)
    amount_to_pay = models.DecimalField(max_length=255, null=True, blank=True, default=0, decimal_places=3, max_digits=15)
    balance = models.DecimalField(max_length=255, null=True, default=0, decimal_places=3, max_digits=15)
    brought_by =  models.CharField(max_length=255, default='', null=True, blank=True)

    CURRENCY_CHOICES = [
        ("USD", '$'),
        ("Ugandan Shillings", 'UGX'),
        ("Naira", '₦'),
        ("Euro", '€'),

       ]
    currency_of_choice = models.CharField(max_length=100,choices=CURRENCY_CHOICES,default='US', null=False, blank=False)

    COUNTRY_CHOICES = [
        ("Australia", 'Australia'),
        ("Canada", 'Canada'),
        ("USA", 'USA'),
        ("Shengen", 'Shengen'),
        ("Israel", 'Israel'),

       ]
    country_of_destination = models.CharField(max_length=100,choices=COUNTRY_CHOICES,default='US', null=True, blank=True)
    nationality = models.CharField(max_length=255, default='', null=True, blank=True) 
    has_paid = models.BooleanField(default=False)
    has_done_biometry_before = models.BooleanField(default=False)
    biometry_date = models.DateField(blank=True, default='', null=True, help_text='')
    has_done_biometry = models.BooleanField(default=False)
    has_obtained_visa_before=models.BooleanField(default=False)
    has_obtained_visa=models.BooleanField(default=False)

    rejected_CHOICES = [
        ('0', '0'),
        ('once', '1'),
        ('twice', '2'),
        ('thrice', '3'),
        ('fourth', '4'),
        ('fith', '5'),
        ]
    rejected = models.CharField(max_length=15, choices=rejected_CHOICES, default='',null=True)
    Departure_date = models.DateField(blank=True, default='', null=True)
    export_to_CSV=models.BooleanField(default=False)

    def get_image(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/assets/img/user.png"
    
    def get_passport(self):
        if self.passport_document and hasattr(self.passport_document, 'url'):
            return self.passport_document.url
        else:
            return "/static/assets/img/user.png"
    
    def __str__(self):
        return self.avatar



    def __str__(self):
        return self.first_name or ''
    
    def get_absolute_url(self):
        return reverse('dashboard:profile', kwargs= {'pk':self.pk} )

    @property
    def full_name(self):
        "returns User's fullname"
        return '%s %s'%(self.first_name,self.last_name)
    
    @property
    def get_amount_paid(self):
        if self.amount_paid_today:
            paid=self.amount_paid_so_far+self.amount_paid_today
            if paid == int(self.amount_to_pay):
                self.has_paid=True
        return paid
    
    @property
    def get_balance(self):
        if self.amount_paid_so_far:
            balance = int(self.amount_to_pay)-int(self.amount_paid_so_far)
            if balance <= 0:
                self.has_paid=True
            return balance

    @property
    def is_due(self):
       if self.biometry_date:
        datetime_object = self.biometry_date
        t2 = datetime.now().date()
        t3 = timedelta(days=30)
        return  datetime_object - t2<= t3
    
    @property
    def is_success(self):
       if self.Departure_date:
        datetime_object = self.Departure_date
        t2 = datetime.now().date()
        return  datetime_object <= t2
        
    



class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)
    evidence_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')


    def __str__(self):
        return str(self.content)

    def get_document(self):
        if self.evidence_document and hasattr(self.evidence_document, 'url'):
            return self.evidence_document.url
        else:
            return "/static/assets/img/user.png"



class AccountsRevenue(models.Model):
    revenue_of = models.CharField(max_length=250, default='Someone paid',null=False)
    revenue_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True )
    amount = models.IntegerField( default='100,000') 
    day_on_which = models.DateField(auto_now=True, null=True, blank=True)
    evidence_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    

    def __str__(self):
        return str(self.revenue_of)

    def get_absolute_url(self):
        return reverse('dashboard:revenue', kwargs= {'pk':self.pk} )

    def get_document(self):
        if self.evidence_document and hasattr(self.evidence_document, 'url'):
            return self.evidence_document.url
        else:
            return "/static/assets/img/user.png"



class AccountsExpense(models.Model):
    expense_of = models.CharField(max_length=250, default='i.e: Transport of a good',null=False)
    expense_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True )
    amount = models.IntegerField( default='') 
    day_on_which = models.DateField(auto_now=True, null=True, blank=True)
    evidence_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')

    def __str__(self):
        return str(self.expense_of)
    
    def get_absolute_url(self):
        return reverse('dashboard:expense', kwargs= {'pk':self.pk} )

    def get_document(self):
        if self.evidence_document and hasattr(self.evidence_document, 'url'):
            return self.evidence_document.url
        else:
            return "/static/assets/img/user.png"




