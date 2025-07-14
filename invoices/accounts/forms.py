from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CompanyProfile, IndividualProfile, BankAccount

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'is_company']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_company'].widget = forms.RadioSelect(choices=[
            (True, 'Company'),
            (False, 'Individual'),
        ])

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name', 'company_code', 'email', 'phone', 'web', 'address', 'vat_code']
        exclude = ['user']

class IndividualProfileForm(forms.ModelForm):
    class Meta:
        model = IndividualProfile
        fields = ['name', 'individual_code', 'email', 'phone', 'web', 'address', 'vat_code']
        exclude = ['user']

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['iban', 'bank_name', 'swift']