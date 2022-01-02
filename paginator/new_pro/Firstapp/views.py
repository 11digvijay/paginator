from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator

def employeeview(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_emp')
    template_name = 'Firstapp/employee.html'
    context = {'form':form}
    return render(request,template_name,context)


def showemployee(request):
    emp_obj = Employee.objects.all()
    paginator = Paginator(emp_obj,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'Firstapp/show.html'
    context = {'page_obj':page_obj}
    return render(request, template_name, context)


def employeeupdate(request,i):
    employee = Employee.objects.get(id=i)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("show_emp")
    template_name = 'Firstapp/employee.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteview(request,i):
    employee = Employee.objects.get(id=i)
    employee.delete()
    return redirect("show_emp")
# Create your views here.
