from django.urls import path
from . import views


urlpatterns = [
    path('category/<int:pk>/', views.job_categories, name='job_categories'),
    path('job/detail/<int:pk>/', views.job_detail, name='job_detail'),

    # post job 
    # path('post/job/', views.postjob, name='post_job'),
    
]