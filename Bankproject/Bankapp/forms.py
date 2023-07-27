from django import forms
from .models import Customer, District, Material

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
#
# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'district', 'branch', 'account_type', 'materials_provide']
        widgets = {'materials_provide': forms.CheckboxSelectMultiple}
