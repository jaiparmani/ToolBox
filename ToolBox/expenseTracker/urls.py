from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [

    path('', lambda request: HttpResponse('Hello World from the app')),
    path("show-all", views.getAllExpenses, name="show_all")
    # path('add/', views.add_expense, name='add_expense'),
    # path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
    # path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
]