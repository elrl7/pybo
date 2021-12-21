from django import forms
from pybo.models import company

class companyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['company_name','company_bisnum', 'expiration_date', 'company_status',
                  'company_address', 'company_email', 'company_note','company_telno']