from rest_framework import serializers
from .models import User, ExpenseCategory, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
    
        model = User
        fields = '__all__'

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = '__all__'