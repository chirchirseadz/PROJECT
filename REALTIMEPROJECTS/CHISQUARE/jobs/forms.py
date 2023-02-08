from django import forms
from .models import Job, jobrequest
from django.forms.widgets import NumberInput


class JobRequestForm(forms.ModelForm):
    class Meta:
        model = jobrequest
        fields = ['proposal', 'experience','support_document','your_budget']
        labels = {
            
            'support_document': 'Supporting Documents',
            'proposal': 'Your brief cover letter',
            'your_budget': 'Amount to be paid (Ksh)'
        }
class PostJobForm(forms.ModelForm):
    job_desc = forms.CharField(widget=forms.Textarea(attrs={'row': 3}))
    dateline =forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Job
        fields = ['area_of_specialization','title','job_desc','budget','vacancy','location','dateline','qualifications','company_details','company_website','terms_of_service','terms_and_conditions']

        labels = {
            'job_desc': 'Describe Your Job',
            'budget': 'Salary to be paid'
        }