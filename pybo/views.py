from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import company
from . forms import companyForm
from django import utils

# Create your views here.

def company_list(request):
    company_list = company.objects.order_by('create_date')
    context = {'company_list': company_list}
    return render(request, 'pybo/company_list.html', context)

@csrf_exempt
def company_list_active(request):
    if 'status' in request.POST:
        print('TEST : ', request.POST['status'])
        status = request.POST['status']
    if status == '1':
        print('TEST status : ', request.POST['status'])
    else:
        print('TEST status : ', request.POST['status'])

    return JsonResponse()

def company_add(request):
    form = companyForm()
    if request.method == 'POST':
        form = companyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.create_date = timezone.now()
            company.save()
            return redirect('pybo:company_list')
    else:
        form = companyForm()
    context = {'form': form}
    return render(request, 'pybo/company_add.html', context)


def company_update(request):

    return render(request, 'pybo/company_update.html')

def department(request):

    return render(request, 'pybo/department.html')

def department_add(request):

    return render(request, 'pybo/department_add.html')

def department_update(request):

    return render(request, 'pybo/department_update.html')

def login(request):

    return render(request, 'pybo/login.html')

def hwh(request):

    return render(request, 'pybo/holiday_work_hour.html')

def bwh(request):
    return render(request, 'pybo/base_work_hour.html')

def holiday(request):
    return render(request, 'pybo/holiday.html')

def money(request):
    return render(request, 'pybo/money.html')

def fix(request):
    return render(request, 'pybo/fix.html')

def non_fix(request):
    return render(request, 'pybo/non_fix.html')

def checkIn_checkOut(request):
    return render(request, 'pybo/checkIn_checkOut.html')

def moneytext(request):
    return render(request, 'pybo/moneytext.html')

def employee_info(request):
    return render(request, 'pybo/employee_info.html')

def annual_use(request):
    return render(request, 'pybo/annual_use.html')

def annual_use_print(request):
    return render(request, 'pybo/annual_use_print.html')

def term_insurance(request):
    return render(request, 'pybo/term_insurance.html')

def retire_pension(request):
    return render(request, 'pybo/retire_pension.html')

def transfer_request(request):
    return render(request, 'pybo/transfer_request.html')

def commute_record(request):
    return render(request, 'pybo/commute_record.html')


