from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet,SavingsGoalViewSet,ExpenseViewSet


router = DefaultRouter()
router.register('incomes', IncomeViewSet, basename='income')
router.register('expenses', ExpenseViewSet, basename='expense')
router.register('savings_goals', SavingsGoalViewSet, basename='savingsgoal')
# router.register('user-financial-summary', user_financial_summary, basename='userfinancialsummary')
# from .views import expense_list

urlpatterns = [
     path('', include(router.urls)),
      #  path('expenseslist/', expense_list, name='expense-list'),
    #  path('user-financial-summary/', user_financial_summary, name='user_financial_summary'),
     
    
]
