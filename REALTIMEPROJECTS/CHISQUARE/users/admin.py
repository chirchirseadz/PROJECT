from django.contrib import admin
from . models import Employer, Applicant, CustomUser

# Register your models here.

admin.site.register(Employer)
admin.site.register(CustomUser)
admin.site.register(Applicant)

