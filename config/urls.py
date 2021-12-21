"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company_list/', include('pybo.urls')),
    path('department/', views.department),
    path('department_add/', views.department_add),
    path('department_update/', views.department_update),
    path('login/', views.login),
    path('hwh/', views.hwh),
    path('bwh/', views.bwh),
    path('holiday/', views.holiday),
    path('money/', views.money),
    path('fix/', views.fix),
    path('non_fix/', views.non_fix),
    path('checkIn_checkOut/', views.checkIn_checkOut),
    path('moneytext/', views.moneytext),
    path('employee_info/', views.employee_info),
    path('annual_use/', views.annual_use),
    path('annual_use_print/', views.annual_use_print),
    path('term_insurance/', views.term_insurance),
    path('retire_pension/', views.retire_pension),
    path('transfer_request/', views.transfer_request),
    path('commute_record/', views.commute_record),
    path('company_list_active/', views.company_list_active),


]
