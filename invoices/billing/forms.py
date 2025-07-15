from django.forms import ModelForm
from .models import Buyer



class BuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'code', 'vat_code', 'address']
