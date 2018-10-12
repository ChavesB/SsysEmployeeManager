from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def employeesList(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employeeList.html', { 'employees': employees })

def employeeEdit(request, pk):
    employee = Employee.objects.get(idemployee=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employeeEdit.html', {'form': form })

def employeeDelete(request, pk):
    employee = Employee.objects.get(idemployee=pk)
    employee.delete()
    return redirect('/')

def employeeNew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employeeEdit.html', { 'form': form })