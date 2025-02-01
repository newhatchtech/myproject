from django import forms

from .models import ConsultationRequest




from django import forms
from .models import InvestmentData

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = InvestmentData
        fields = ['investment_amount', 'payment_method', 'additional_info', 'first_name', 'last_name', 'email', 'phone_number']
