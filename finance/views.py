# personal_finance_management/views.py

from rest_framework import viewsets
from .models import Income, Expense, SavingsGoal
from .serializers import IncomeSerializer, ExpenseSerializer, SavingsGoalSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.db.models import Sum


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # Log the incoming request data
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    def create(self, request, *args, **kwargs):
        print(request.data)  # Log the incoming request data
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
   

class SavingsGoalViewSet(viewsets.ModelViewSet):
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingsGoalSerializer
    def create(self, request, *args, **kwargs):
        print(request.data)  # Log the incoming request data
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset





   
