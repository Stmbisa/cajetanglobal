from django.db import models
from users.models import AccountsExpense, Profile, User
from django.urls import reverse


TRANSACTION_STATUS = [
        ("in", 'in'),
        ("out", 'out'),]

class Transactions(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True )
    Transaction_date = models.DateField( null=True, blank=True)
    amount_paid_or_paying = models.CharField(max_length=250, default='',null=False)
    status = models.CharField(max_length=10, choices=TRANSACTION_STATUS,default='', null=True, blank=True)
    reason = models.CharField(max_length=250, default='',null=False)

    def __str__(self):
        return self.profile


    def get_absolute_url(self):
        return reverse('dashboard:transaction', kwargs= {'pk':self.pk} )



    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = '.'
    #     verbose_name_plural = '.s')


class ProfileEvents(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True )
    event_name= models.CharField(max_length=100, default='', null=True, blank=True) 
    event_date = models.DateField( null=True, blank=True)

    def get_absolute_url(self):
        return reverse('dashboard:event', kwargs= {'pk':self.pk} )

    def __str__(self):
        return self.profile
