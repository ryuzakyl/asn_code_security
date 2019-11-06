from django import forms


class CsrfForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=50, required=False)


class XssForm(forms.Form):
    malicious_data = forms.CharField(max_length=100, required=True)
