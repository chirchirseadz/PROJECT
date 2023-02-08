from django import forms
from . models import Applicant, Employer, CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
     

        
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
            'is_staff' : 'Register As Employer',
            'first_name': 'First Name'
        }






class EmployeeSignUpForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
     

        
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
            'first_name': 'First Name'
        }




class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email',]


class EmployeeProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['national_id','job_title','address','phone','current_location','image']
        labels = {
            
            'brief_info': 'Talk About Yourself',
            
        }

class EmployerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['national_id','job_title','address','phone','current_location','company_name','company_email','image']

        labels = {
            
            'brief_info': 'About Yourself',
            'profile_updated': 'Update completed ?'
        }


