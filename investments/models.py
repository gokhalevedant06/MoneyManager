from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BANK_NAMES = [
    ('Public Sector Banks', (
        ('Bank of Maharashtra', 'Bank of Maharashtra'),
        ('Bank of Baroda', 'Bank of Baroda'),
        ('Bank of India', 'Bank of India'),
        ('Canara Bank', 'Canara Bank'),
        ('Central Bank of India', 'Central Bank of India'),
        ('IDBI Bank', 'IDBI Bank'),
        ('Indian Bank', 'Indian Bank'),
        ('Indian Overseas Bank', 'Indian Overseas Bank'),
        ('Punjab National Bank', 'Punjab National Bank'),
        ('Punjab & Sind Bank', 'Punjab & Sind Bank'),
        ('State Bank of India', 'State Bank of India'),
        ('UCO Bank', 'UCO Bank'),
        ('Union Bank', 'Union Bank')
    )),
    ('Private Sector Banks', (
        ('Axis Bank', 'Axis Bank'),
        ('Bandhan Bank', 'Bandhan Bank'),
        ('Catholic Syrian', 'Catholic Syrian'),
        ('City Union Bank', 'City Union Bank'),
        ('DCB Bank', 'DCB Bank'),
        ('Dhanlaxmi Bank', 'Dhanlaxmi Bank'),
        ('Federal Bank', 'Federal Bank'),
        ('HDFC Bank', 'HDFC Bank'),
        ('ICICI Bank', 'ICICI Bank'),
        ('IDFC First Bank', 'IDFC First Bank'),
        ('IndusInd Bank', 'IndusInd Bank'),
        ('J & K Bank', 'J & K Bank'),
        ('Karnataka Bank', 'Karnataka Bank'),
        ('Kotak Bank', 'Kotak Bank'),
        ('Karur Vysya Bank', 'Karur Vysya Bank'),
        ('RBL Bank', 'RBL Bank'),
        ('South Indian Bank', 'South Indian Bank'),
        ('Tamilnad Mercantile Bank', 'Tamilnad Mercantile Bank'),
        ('TNSC Bank', 'TNSC Bank'),
        ('Yes Bank', 'Yes Bank'),
    ))
]

TIME_CHOICES = [
    ('short', '1 to 5 Years'),
    ('medium', '5 to 15 Years'),
    ('long', '15 Years & above'),
]


class Schemes(models.Model):
    bank_name = models.CharField(max_length=100, choices=BANK_NAMES)
    scheme = models.CharField(max_length=100)

    def __str__(self):
        return "%s  :  %s" % (self.bank_name, self.scheme)


class SchemeRates(models.Model):
    scheme_name = models.ForeignKey(Schemes, on_delete=models.CASCADE)
    intrest_rate = models.FloatField()
    time_span = models.CharField(choices=TIME_CHOICES, max_length=100)


class InvestmentInfo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="investment_info")
    scheme_name = models.ForeignKey(Schemes, on_delete=models.CASCADE)
    invested_amount = models.IntegerField()
    timespan = models.IntegerField()
    intrest_payout = models.IntegerField(default=0)
    maturity_date = models.DateField(auto_now=True)
