from django import forms
from .models import Person

class NameForm(forms.Form):
    num1=forms.CharField(label="NuM1", max_length=20)
    num2=forms.CharField(label="num2", max_length=20)
