
from django import forms

class CalculatorForm(forms.Form):
    value=forms.CharField(label='Enter Value :',widget=forms.TextInput(attrs={'class':'value','placeholder':'Enter Value'}))
    