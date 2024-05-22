from django.contrib import admin
from .models import Income, Expense, SavingsGoal,Profile

admin.site.register(Profile)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(SavingsGoal)