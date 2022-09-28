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
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)



class User(AbstractUser):
    is_verified= models.BooleanField(default=False) 
    has_taken_biometry_before= models.BooleanField(default=False)
    avatar = models.ImageField(upload_to = 'uploads/', default='')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    # GENDER_MALE = 'Male'
    # GENDER_FEMALE = 'Female'
    # OTHER = 'Other'

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
       ]
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES,null=False,default='', blank=False)
    username=models.EmailField(unique=True, null=True)
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
    next_of_kin = models.CharField(max_length=255, default='')
    next_of_kin_phone_number = models.CharField(max_length=14, default='')
    
    
    objects: UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username or ''
        # return self.first_name+ ' ' + str(self.last_name)
    @property
    def full_name(self):
        "returns User's fullname"
        return '%s %s'%(self.first_name,self.last_name)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    has_passport = models.BooleanField(default=False)
    passport_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
       ]

    
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='',null=False)
    email = models.EmailField(default='none@email.com')
    phonenumber = models.CharField(max_length=15,null=False, default='') #blank=True, null=True
    birth_date = models.DateField(blank=True, default='', null=False)
    next_of_kin = models.CharField(max_length=255, default='',)
    next_of_kin_phone = models.IntegerField(unique=True)
    country_of_orgin = models.CharField(max_length=255, default='', null=False)
    amount_paid_so_far= models.DecimalField(max_length=255, null=False,default=0, decimal_places=3, max_digits=15)
    amount_paid_today= models.DecimalField(max_length=255, null=False,default=0, decimal_places=3, max_digits=15)
    amount_to_pay = models.DecimalField(max_length=255, null=False, default=0, decimal_places=3, max_digits=15)
    balance = models.DecimalField(max_length=255, null=False, default=0, decimal_places=3, max_digits=15)
    brought_by =  models.CharField(max_length=255, default='', null=False)

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
    country_of_destination = models.CharField(max_length=100,choices=COUNTRY_CHOICES,default='US', null=False, blank=False)
    nationality = models.CharField(max_length=255, default='') 
    has_paid = models.BooleanField(default=False)
    has_done_biometry_before = models.BooleanField(default=False)
    biometry_date = models.DateField(blank=True, default='', null=True)
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
            return 'path/to/default/image'
    
    def __str__(self):
        return self.avatar



    def __str__(self):
        return self.user.username or ''
    
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
            balance=self.amount_to_pay-self.amount_paid_so_far
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
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/assets/img/user.png"




class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)
    evidence_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')


    def __str__(self):
        return str(self.content)



class Accounts_revenue(models.Model):
    revenue_of = models.CharField(max_length=100, default='i.e: visa payment',null=False)
    revenue_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True )
    amount = models.IntegerField( default='') 
    day_on_which = models.DateField(auto_now=True, null=True, blank=True)
    evidence_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    

    def __str__(self):
        return str(self.revenue_of)

    def get_absolute_url(self):
        return reverse('dashboard:revenue', kwargs= {'pk':self.pk} )

    @property
    def get_sum(self):
        tot = 0
        return (tot + self.amount  )


class Accounts_expense(models.Model):
    expense_of = models.CharField(max_length=250, default='i.e: Trnsport',null=False)
    expense_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True )
    amount = models.IntegerField( default='') 
    day_on_which = models.DateField(auto_now=True, null=True, blank=True)
    evidence_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')

    def __str__(self):
        return str(self.expense_of)
    
    def get_absolute_url(self):
        return reverse('dashboard:revenue', kwargs= {'pk':self.pk} )




