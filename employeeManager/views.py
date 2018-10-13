from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Employee
from .forms import EmployeeForm
import json

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


#API DJANGO com as funcionalidades listar, adicionar e remover
from django.views.decorators.csrf import csrf_exempt

def employeeList(request):
    resp = [{ 'name':employee.name, 'email': employee.email, 'department': employee.department } for employee in Employee.objects.all()]
    resp_json = json.dumps(resp)
    return HttpResponse(resp_json, content_type='application/json')

@csrf_exempt
def employeeAdd(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'add': 'success'})
    return JsonResponse({'add': 'failed'})

@csrf_exempt
def employeeRemove(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee = Employee.objects.get(name=employee.name, email=employee.email, department=employee.department)
            employee.delete()
            return JsonResponse({'remove': 'success'})
    return JsonResponse({'remove': 'failed'})