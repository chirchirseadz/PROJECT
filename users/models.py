from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):
    PROFFESION = (
        ('IT specialist', 'IT specialist'),
        ('Web Design','Web Design'),
        ('Nanny', 'Nanny'),
     

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    proffesion = models.CharField(max_length=20, choices=PROFFESION, default=None)
    description = models.TextField(blank=True, verbose_name='Brief Description' )
    address = models.CharField(max_length=255, null=True, verbose_name='Location Address')
    phone  = models.CharField(max_length=20, null=True, verbose_name='Mobile Phone Number')
    image  = models.ImageField(default='', upload_to='images/', verbose_name='Profile picture') 

    def __str__(self):
        return self.user.username 