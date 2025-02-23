from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=10)
    def __str__(self):
        return str(self.id)+self.name

    
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)+ self.name
    
class Expense(models.Model):
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    expense_category = models.ForeignKey('ExpenseCategory', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id)+self.description
