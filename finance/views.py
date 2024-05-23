# personal_finance_management/views.py

from rest_framework import viewsets
from .models import Income, Expense, SavingsGoal
from .serializers import IncomeSerializer, ExpenseSerializer, SavingsGoalSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from django_filters.rest_framework import DjangoFilterBackend

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
    











# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Expense
# from .serializers import ExpenseSerializer
# from django.core.paginator import Paginator
# from django.db.models import Sum
# from datetime import datetime

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def expense_list(request):
#     user = request.user
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')

#     expenses = Expense.objects.filter(user=user)
    
#     if start_date:
#         start_date = datetime.strptime(start_date, '%Y-%m-%d')
#         expenses = expenses.filter(date__gte=start_date)
    
#     if end_date:
#         end_date = datetime.strptime(end_date, '%Y-%m-%d')
#         expenses = expenses.filter(date__lte=end_date)
    
#     paginator = Paginator(expenses, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     serializer = ExpenseSerializer(page_obj, many=True)
#     total_pages = paginator.num_pages
    
#     return Response({
#         'results': serializer.data,
#         'total_pages': total_pages,
#         'total_expense': expenses.aggregate(Sum('amount'))['amount__sum'] or 0
#     })





   
