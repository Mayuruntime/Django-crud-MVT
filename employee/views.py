from django.shortcuts import render, redirect, HttpResponse
from .models import Employee
from .forms import EmployeeForm

# from django.core.mail import send_mail
# from main.settings import DATABASES, EMAIL_HOST_USER, TIME_ZONE
# import requests
# import smtplib , ssl

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

    # message = f"""Runtime Solution Welcomes You \n\n USERNAME:  "Mayur" \n PASSWORD:  "helloMayur" """
    # recepient = "mayur.runtime@gmail.com"     
    # # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)  

    # url = "http://127.0.0.1:8000/"
    # payload={}
    # headers = {}
    # response = requests.request("GET", url, headers=headers, data=payload)
    # while True:
    #     # sending mail
    #     server = smtplib.SMTP("smtp.falconide.com",587)
    #     server.ehlo()
    #     server.starttls
    #     server.login("runtimefal","Runtime@2022")
    #     server.sendmail("noreply@runtime-solutions.com" , recepient , message)
    #     server.quit()
    #     # checkAPiServerAvilableOrNot()
    #     # time.sleep(1000)       
    #     break 


    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        Employee.objects.filter(id=id).update(is_deleted=True,is_active=False)
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)