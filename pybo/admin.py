from django.contrib import admin
from .models import company
# Register your models here.


class companyAdmin(admin.ModelAdmin):
    search_fields = ['company_name']

admin.site.register(company, companyAdmin)