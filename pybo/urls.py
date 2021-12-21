from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('/company_add/', views.company_add, name='company_add'),
    path('/company_update/', views.company_update, name='company_update'),
    path('', views.department, name='department'),
    path('/department_add/', views.department_add, name='department_add'),
    path('/department_update/', views.department_update, name='department_update'),

]
