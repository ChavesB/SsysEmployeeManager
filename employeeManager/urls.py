from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeesList, name='employeesList'),
    path('employee/<int:pk>/edit/', views.employeeEdit, name='employeeEdit'),
    path('employee/<int:pk>/delete/', views.employeeDelete, name='employeeDelete'),
    path('employee/new', views.employeeNew, name='employeeNew'),
    path('employee/', views.employeeList, name='list'),
    path('employee/add/', views.employeeAdd, name='add'),
    path('employee/remove/', views.employeeRemove, name='remove'),
]
