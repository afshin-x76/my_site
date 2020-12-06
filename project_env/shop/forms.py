from django import forms
from .models import BillingAddress



class CheckOutForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['state', 'address', 'phone_number', 'plaque']
        widgets = {
            'state': forms.Select(attrs={'class':'custom-select d-block w-100'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'plaque': forms.TextInput(attrs={'class': 'form-control'}),
        }

