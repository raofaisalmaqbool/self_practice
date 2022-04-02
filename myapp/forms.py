from django import forms


class UserForms(forms.Form):
    num1 = forms.CharField(label='value 1', required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    num2 = forms.CharField(label='value 2')
    num3 = forms.CharField()
    # email = forms.EmailField()