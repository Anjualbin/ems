from django.forms import ModelForm
from employer.admin import UserCreationForm
from employer.models import MyUser
from django import forms

class AddEmployeeForm(UserCreationForm):
    password1: forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2: forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model=MyUser
        fields=['first_name','last_name',"email","role","password1","password2","image"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "role": forms.Select(attrs={"class":"form-select","readonly":True}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"})
         }