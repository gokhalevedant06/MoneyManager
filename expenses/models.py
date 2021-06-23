from django.db import models
from django.contrib.auth.models import User

# Create your models here.

EXPENSES = [
    ('Electricity Bill', 'Electricity Bill'),
    ('Groceries', 'Groceries'),
    ('Shopping', 'Shopping'),
    ('Rent', 'Rent'),
    ('Loan', 'Loan'),
    ('Fitness', 'Fitness'),
    ('Transport', 'Transport'),
]


class ExpenseData(models.Model):
    user = models.ForeignKey(User, related_name="expensedata",
                             on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=100)
    expense_amount = models.IntegerField()
    remaining_amount = models.IntegerField()
    time = models.DateField(auto_now=True)
