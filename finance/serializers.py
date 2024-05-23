from rest_framework import serializers
from .models import Income, Expense, SavingsGoal

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

    # def create(self, validated_data):
    #     income = Income.objects.create(**validated_data)
    #     profile = income.user.profile
    #     profile.balance += income.amount
    #     profile.save()
    #     return income

    # def update(self, instance, validated_data):
    #     profile = instance.user.profile
    #     profile.balance -= instance.amount
    #     profile.balance += validated_data.get('amount', instance.amount)
    #     profile.save()
    #     return super().update(instance, validated_data)

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    # def create(self, validated_data):
    #     expense = Expense.objects.create(**validated_data)
    #     profile = expense.user.profile
        
    #     profile.balance -= expense.amount
      
    #     profile.save()
    #     return expense

    # def update(self, instance, validated_data):
    #     profile = instance.user.profile
    #     profile.balance += instance.amount
    #     profile.balance -= validated_data.get('amount', instance.amount)
    #     profile.save()
    #     return super().update(instance, validated_data)

class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = '__all__'
