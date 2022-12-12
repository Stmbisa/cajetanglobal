from django.db import models
from users.models import AccountsExpense, Profile, User
from django.urls import reverse
from datetime import datetime, timedelta
from datetime import *
from django.utils import timezone

TRANSACTION_STATUS = [
        ("in", 'in'),
        ("out", 'out'),
        ("pending", 'pending'),
        ]

class Transactions(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )
    Transaction_date = models.DateField( null=True, blank=True)
    amount_paid_or_paying = models.CharField(max_length=250, default='',null=False)
    amount_to_pay = models.DecimalField(max_length=255, null=True, blank=True, default=0, decimal_places=3, max_digits=15)
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS,default='', null=True, blank=True)
    reason = models.CharField(max_length=250, default='',null=False)

    def __str__(self):
        return self.profile


    def get_absolute_url(self):
        return reverse('dashboard:transaction', kwargs= {'pk':self.pk} )

    def get_balance (self):
        if self.amount_to_pay and self.amount_paid_or_paying:
            balance=int(self.amount_to_pay)
            balance=-int(self.amount_paid_or_paying)
            return balance



    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = '.'
    #     verbose_name_plural = '.s')


class ProfileEvents(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )
    event_name= models.CharField(max_length=100, default='', null=True, blank=True) 
    event_date = models.DateField( null=True, blank=True)

    def get_absolute_url(self):
        return reverse('dashboard:event', kwargs= {'pk':self.pk} )

    def __str__(self):
        return self.profile

    @property
    def is_due(self):
       if self.event_date:
        datetime_object = self.event_date
        t2 = datetime.now().date()
        t3 = timedelta(days=15)
        return  datetime_object - t2<= t3
    @property
    def is_passed(self):
       if self.event_date:
        datetime_object = self.event_date
        t2 = datetime.now().date()
        t3 = timedelta(days=0)
        return  datetime_object - t2>= t3



class Cashmemo(models.Model):
    cashmemo_of = models.CharField(max_length=250, default='i.e: Repair fee',null=True)
    cashmemo_by = models.CharField(max_length=250, default='i.e: The name of the person',null=False)
    amount = models.IntegerField( default='0') 
    day_on_which = models.DateField(null=True, blank=True)
    evidence_document = models.ImageField(upload_to = 'uploads/', blank=True, default='')
    signature = models.ImageField(upload_to = 'uploads/', blank=True, default='')

    def __str__(self):
        return str(self.expense_of)
    
    def get_absolute_url(self):
        return reverse('dashboard:expense', kwargs= {'pk':self.pk} )

    def get_document(self):
        if self.evidence_document and hasattr(self.evidence_document, 'url'):
            return self.evidence_document.url
        else:
            return "/static/assets/img/user.png"




class Documents(models.Model):
    document_owner = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=False )
    document_name = models.CharField(max_length=250, default='i.e: passport',null=True)
    date_submitted = models.DateField(null=True, blank=True)
    document = models.FileField(upload_to = 'uploads/', blank=True, default='')


    def __str__(self):
        return str(self.document_name)

    def get_absolute_url(self):
        return reverse('dashboard:document', kwargs= {'pk':self.pk} )

    def get_document(self):
        if self.document and hasattr(self.document, 'url'):
            return self.document.url
        else:
            return "/static/assets/img/user.png"