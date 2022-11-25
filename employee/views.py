from django.shortcuts import render, redirect, HttpResponse
from .models import Employee
from .forms import EmployeeForm

def employees_list(request):
    employees = Employee.objects.filter(is_deleted=False,is_active=True)
    context = {
        'employees': employees,
    }
    return render(request, 'employee/list.html', context)

def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'form': form,
    }
    return render(request, 'employee/create.html', context)


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee/edit.html', context)


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        Employee.objects.filter(id=id).update(is_deleted=True,is_active=False)
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)