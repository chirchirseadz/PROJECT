from django import forms
from django.contrib.auth.models import User

from . models import user_profile
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff',)
     

        
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
            'is_staff' : 'Register As Employer',
            'first_name': 'First Name'
        }


    class user_profile(forms.ModelForm):
    
        bio = forms.CharField()
        profile_pic = forms.ImageField() 

        nanny = 'nanny',
        employer = 'employer'

        user_types = (

            (nanny,'nanny'),
            (employer,'Employer'),

        )
        user_type = forms.ChoiceField(required=True, choices=user_types)





        widgets = {
            'username' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Username'
                
                }),
            'first_name' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'First Name'
                
                }),
            'last_name' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Last Name'
                }),
            'email' : forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'Email '
                }),
            'password1' : forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder': 'Password'
                }),
            'password2' : forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder': 'Confirm Password'
                }),
            
        }
