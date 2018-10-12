from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeesList, name='employeeList'),
    path('employee/<int:pk>/edit/', views.employeeEdit, name='employeeEdit'),
    path('employee/<int:pk>/delete/', views.employeeDelete, name='employeeDelete'),
    path('employee/new', views.employeeNew, name='employeeNew'),
]
