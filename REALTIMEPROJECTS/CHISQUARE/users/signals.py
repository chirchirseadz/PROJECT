from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  CustomUser
 
# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         CustomUser.objects.create(email=instance)
    
# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     instance.CustomUser.save()

