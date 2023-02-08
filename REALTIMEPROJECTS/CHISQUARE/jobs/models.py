from django.db import models
from django.urls import reverse
# from users.models import user_profile

from users.models import Applicant, Employer,CustomUser
# Create your models here.

class AreaOfSpecialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_urls(self):    
        return reverse('area_of_specialization', args=[self.id])
   

class Job(models.Model):
    TERMS_OF_SERVICE = (
        ('Contract','Contract'),
        ('Temporary','Temporary'),
        ('Permanent','Permanent'),
        
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    area_of_specialization= models.ForeignKey(AreaOfSpecialization, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    job_desc =  models.TextField(blank=False)
    budget =  models.FloatField()
    vacancy = models.PositiveIntegerField(default=1, null=True)
    location = models.CharField(max_length=100, null=True)
    qualifications = models.TextField(null=True)
    company_details = models.TextField(null=True)
    company_website = models.URLField(null=True)
    terms_of_service = models.CharField(max_length=100, choices=TERMS_OF_SERVICE, null=True)
    dateline = models.DateField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    terms_and_conditions = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_urls(self):    
        return reverse('area_of_specialization', args=[self.id])
   

class jobrequest(models.Model):
    EXPERIENCE = (
        ('less than 1(yr)','less than 1(yr)'),
        ('1-2 (yrs)','1-2 (yrs)'),
        ('3-4 (yrs)','3-4 (yrs)'),
        ('Above 5yrs','Above 5yrs'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    proposal = models.TextField(blank=False)
    experience = models.CharField(max_length=100, choices=EXPERIENCE, null=True)
    support_document = models.FileField(null=True)
    your_budget = models.FloatField(null=True)
    
    def __str__(self):
        return f'{self.job} job requested by {self.user}'