from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from .models import Expense, ExpenseCategory
# Create your views here.

from .serializers import ExpenseCategorySerializer, ExpenseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def getAllExpenses(request):
    return HttpResponse("Hello")

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/subject-list/',
        # 'Detail View': '/subject-detail/<str:pk>/',
        # 'Create': '/subject-create/',
        # 'Update': '/subject-update/<str:pk>/',
        # 'Delete': '/subject-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['POST'])
# application/json
def createExpense(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=400)
    return Response(serializer.data)
# payload for add-expense
# {
#     "amount": 100,
#     "description": "test",
#     "expense_category": 1,
#     "user": 1
# }


class UserExpenseView(View):
    def get(self, request, user_id):
        expenses = Expense.objects.filter(user_id=user_id)
        expense_data = list(expenses.values())
        return JsonResponse({'expenses': expense_data})
    # def post(self, request, user_id):
    #     serializer = ExpenseSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()   
    #     else:
    #         return Response(serializer.errors, status=400)
    #     return Response(serializer.data)
            