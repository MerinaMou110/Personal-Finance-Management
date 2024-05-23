# personal_finance_management/models/income.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.amount}"



class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.amount}"



class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.description} - {self.target_amount}"
    


