from django.contrib import admin
from .models import AreaOfSpecialization, Job, jobrequest

# Register your models here.

admin.site.register(AreaOfSpecialization)

admin.site.register(Job)

admin.site.register(jobrequest)