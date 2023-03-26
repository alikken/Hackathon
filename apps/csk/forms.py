from django import forms 

from .models import (
    UserCall,
)


class UserCallForm(forms.ModelForm):
    """UserCall form."""

   
        
    class Meta:
        abstract = True
        model = UserCall
        exclude = ('master_id', 'caller', 'service', 'status',)
        widgets = {
            'personal_account': forms.NumberInput(attrs={'id': 'personal_account', 'class': 'form-control'}),
            'problem': forms.Textarea(attrs={'id': 'problem', 'class': 'form-control'}),
        }


class UserCallUpdateForm(forms.ModelForm):
    """UserCallUpdate form."""

    class Meta:
        model = UserCall
        fields = "__all__"

        

class UserCallForm2(forms.ModelForm):
    """UserCall form."""

   
        
    class Meta:
        abstract = True
        model = UserCall
        fields = ("personal_account", "problem",)
        widgets = {
            'personal_account': forms.NumberInput(attrs={'id': 'personal_account', 'class': 'form-control'}),
            'problem': forms.Textarea(attrs={'id': 'problem', 'class': 'form-control'}),
        }

