from django.db import models

class Destination(models.Model):
    country = models.CharField(max_length=150)
    WV = 'Working Visa'
    TV = 'Touring Visa'
    SV = 'Studying Visa'
    DV = 'Diplomatic Visa'
    PR = 'Permanent Residence'

    VISA_TYPES = [
        (WV, 'Working Visa'),
        (TV, 'Touring Visa'),
        (SV, 'Studying Visa'),
        (DV, 'Diplomatic Visa'),
        (PR, 'Permanent Residence'),

       ]
    type_of_visa = models.CharField(max_length=100,choices=VISA_TYPES,default='US', null=False, blank=False)
    reason = models.CharField(max_length=150)
    price = models.IntegerField()
