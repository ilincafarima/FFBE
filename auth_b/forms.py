from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=100, required=True)
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    dob = forms.DateField(required=True)
    role = forms.ChoiceField(choices=(('Fixer', 'Fixer'), ('Client', 'Client')), required=True)
    fixer_job = forms.CharField(max_length=20, required=False)  # Optional field for Fixer job
    
    class Meta:
        model = CustomUser  # Use CustomUser model
        fields = ['username', 'email', 'password1', 'password2', 'location', 'name', 'surname', 'dob', 'role', 'fixer_job']

    def clean_role(self):
        role = self.cleaned_data.get('role')
        fixer_job = self.cleaned_data.get('fixer_job')

        if role == 'Fixer' and not fixer_job:
            raise forms.ValidationError("Fixer job must be specified for Fixers")
        
        return role

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)

class ModifyForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
