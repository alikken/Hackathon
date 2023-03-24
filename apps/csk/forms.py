from django import forms 

from .models import UserCall, AdminCall


class UserCallForm(forms.ModelForm):
    """UserCall form."""

    class Meta:
        model = UserCall
        fields = (
            'caller',
            'problem'
        )


class AdminCallForm(forms.ModelForm):
    """UserCall form."""

    class Meta:
        model = AdminCall
        fields = (
            'user_call',
            'service_type'
        )

        