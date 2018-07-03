from django import forms
from .models import *


class contactform(forms.ModelForm):
    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)

    class Meta:
        model=Info
        fields=['first_name','last_name']
        #fields='__all__'
    







   
