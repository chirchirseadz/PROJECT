from django.shortcuts import render, redirect
from .forms import JobRequestForm, PostJobForm
from .models import AreaOfSpecialization, Job
from django.http import HttpResponse

# Create your views here.

def area_of_specialization(request):
    return {
        'area_of_specialization': AreaOfSpecialization.objects.all()
    }

def job_categories(request, pk):
    category = AreaOfSpecialization.objects.get(id=pk)
    job = Job.objects.filter(area_of_specialization=category)
    job_count = Job.objects.filter(area_of_specialization=category).count()

    context = {
        'jobs': job,
        'job_count': job_count,
        'category': category
    }
    return render(request, 'jobs/job_category.html', context)

def job_detail(request, pk):
    try:
        job = Job.objects.get(id=pk)
        # job_request = jobrequest.objects.all()
        if request.method == "POST":
            data = JobRequestForm(request.POST, )
            if data.is_valid():
                form = data.save(commit=False)
                form.user = request.user
                form.job=job
                form.proposal=request.POST['proposal']
                form.experience=request.POST['experience']
                form.your_budget=request.POST['your_budget']
                form.save()
        else:
            form = JobRequestForm()
           

        context = {
            'job': job,
            'form': form
        }
        return render(request, 'jobs/job_detail.html', context)
    except:
        return redirect('user-dashboard')
    
#  POST JOB FUNCTION 
def postjob(request):
    if request.method == 'POST':
        post_job_form = PostJobForm(request.POST)
        if post_job_form.is_valid():
            post_job_form.save()
    else:
        post_job_form = PostJobForm()
    context = {
        'post_job_form': post_job_form
    }
    return render(request, 'jobs/post_job.html',context)