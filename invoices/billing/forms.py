from django.forms import ModelForm
from django import forms
from .models import Buyer, Invoice


class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'code', 'vat_code', 'address']


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['buyer', 'series', 'number', 'issue_date', 'due_date', 'include_vat']
        widgets = {
            'issue_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'include_vat': forms.RadioSelect(choices=[
                (True, 'Yes, include VAT'),
                (False, 'No, VAT not applicable'),
            ]),
        }