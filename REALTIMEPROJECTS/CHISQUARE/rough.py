# # write a django code to schedule an interview with job seekers

# #1

# from django.db import models

# class Interview(models.Model):
#     job_seeker = models.ForeignKey('JobSeeker', on_delete=models.CASCADE)
#     interviewer = models.ForeignKey('Interviewer', on_delete=models.CASCADE)
#     job = models.ForeignKey('job', on_delete=models.CASCADE, null=True)
#     date_scheduled = models.DateField()
#     time_scheduled = models.TimeField()

# #2

# from django.shortcuts import render, redirect
# from . models import Interview

# def schedule_interview(request):
#     if request.method == 'POST':
#         job_seeker = request.POST.get('job_seeker')
#         interviewer = request.POST.get('interviewer')
#         date_scheduled = request.POST.get('date_scheduled')
#         time_scheduled = request.POST.get('time_scheduled')
#         Interview.objects.create(job_seeker=job_seeker, interviewer=interviewer, date_scheduled=date_scheduled, time_scheduled=time_scheduled
# continue #3

# #3

# def confirmation(request):
#     return render(request, 'confirmation.html')

# continue #4

# #4

# def success(request):
#     return redirect('confirmation.html')
# continue #5

# #5

# def failure(request):
#     return render(request, 'failure.html')
# continue  #6

# #6

# def goodbye(request):
#     return redirect('failure.html')
# continue  #7

# #7

# def thank_you(request):
#     return render(request, 'thank_you.html')

# continue  #8

# #8

# def goodbye_again(request):
#     return redirect('thank_you.html')
# continue  #9

# #9

# def main(request):
#     return render(request, 'main.html')

# continue  #10

# #10

# def goodbye_main(request):
#     return redirect('main.html')