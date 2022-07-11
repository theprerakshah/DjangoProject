from django import forms

class NameForm(forms.Form):
    empname = forms.CharField(label='empname', max_length=100)
    empid = forms.CharField(label='empid', max_length=100)
    empdept = forms.CharField(label='empdept', max_length=100)
    empphone = forms.CharField(label='empphone', max_length=100)
    
