from django import forms
from django.forms import ModelForm


class NameForm(forms.Form):
    current_courses = forms.CharField(label='current_courses', max_length=100)
    pref_location = forms.CharField(label = 'pref_location')
    pref_salary = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '10', 'max': '200', 'id':'pref_salary'}), required=False)