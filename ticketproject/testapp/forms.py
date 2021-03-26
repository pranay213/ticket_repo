from django import forms
from testapp.models import TicketSignup

class TicketSignupForm(forms.ModelForm):
    class Meta:
        model=TicketSignup
        fields='__all__'
