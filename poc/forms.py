import datetime
from django import forms
from django.core.exceptions import ValidationError


class CsrfForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=50, required=False)


class XssForm(forms.Form):
    malicious_data = forms.CharField(max_length=100, required=True)


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(required=True, help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        # get cleaned data with default validators
        data = self.cleaned_data['renewal_date']

        # check date is not in past.
        if data < datetime.date.today():
            raise ValidationError('Invalid date - renewal in past')

        # check date is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # remember to always return the cleaned data.
        return data
