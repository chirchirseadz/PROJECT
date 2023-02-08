from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import MessageForm,AdminUserEditForm
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail 
from django.http import HttpResponse

from jobs.models import Job, jobrequest

# Create your views here.

def landing_page(request):
  
    return render(request, 'dashboard/landing_page.html')


@login_required(login_url='login')
def index(request):
    users = CustomUser.objects.filter(is_admin=False)
    jobs = Job.objects.all()
    job_count = jobs.count()

    job_requests = jobrequest.objects.all()
    job_requests_count = job_requests.count()
    number_of_users = users.count()
    context = {
        'users': users,
        'jobs': jobs,
        'job_count': job_count,
        'job_requests': job_requests,
        'job_requests_count': job_requests_count,
        'number_of_users':number_of_users
    }
    return render(request, 'dashboard/index.html', context)

def list_of_users(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
        
    }
    return render(request, 'users/partials/users.html', context)


def edit_user(request, id):
    user_obj = CustomUser.objects.get(id=id)
    form = AdminUserEditForm(request.POST, instance=user_obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'User details updated Successfully !!!' )
            return redirect('list_of_users')
    else: 
        form = form = AdminUserEditForm(instance=user_obj)
    context = {
        'form' : form 
    }
    return render(request, 'users/partials/edit_user.html', context)


# def edit_user(request, pk):
#     user_obj = CustomUser.objects.get(id=pk)
#     form = AdminUserEditForm(instance=user_obj)
#     if request.method == 'POST':
#         if form.is_valid(): 
#             form.save()
#             # return redirect('list_of_users')
#             return HttpResponse('User update successfull')
#     else:
#         form = AdminUserEditForm(instance=user_obj)
#         return redirect('list_of_users')
#     context = {
#        'form' :form,
#     }
#     return render(request, 'users/partials/edit_user.html', context)



























def about(request):
    
    return render(request, 'dashboard/about.html')


def blog(request):
    return render(request, 'dashboard/blog.html')



def contact(request):
    if request.method == 'POST':
        # message_sent = False
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            your_name = message_form.cleaned_data.get('your_name')
            email = message_form.cleaned_data.get('email')
            subject = message_form.cleaned_data.get('subject')
            message = message_form.cleaned_data.get('message')
            message_form.save()

            send_mail(


                subject,  # subject 
                message,  # message   
                email, # from 
                ['info@chi-squareconnections.com'], # To email 
                # "This is the message from  chisquare-connections  contact us page ", 
                fail_silently = False
                
                 
            )

            # message_sent = True

            messages.success(request, 'Your message was sent successfully !')

            return redirect('contact')
        

            # return HttpResponse('<script> window.alert("Thanks for your comment")</script>')
    else:
        message_form = MessageForm()
        your_name = MessageForm()
    context = {
        'message_form': message_form,
        'your_name':your_name
    }
    return render(request, 'dashboard/contact.html', context)



def news_and_notices(request):

    return render(request, 'dashboard/news_and_notices.html')


def testimonials(request):
    return render(request, 'dashboard/testimonials.html')





    
################### talent works ###########

# def admin_assistant(request):
#     users = User.objects.all()
#     context = {
#         'users' : users
#     }
#     return render(request, 'dashboard/admin_assistant.html',context)

# def clerk_data_entry(request):
#     return render(request, 'dashboard/clerk_data_entry.html')


# def it_spacialist(request):
#     return render(request, 'dashboard/it_spacialist.html')

# def hospitality(request):
#     return render(request, 'dashboard/hospitality.html')


# def customer_care(request):
#     return render(request, 'dashboard/customer_care.html')

# def hospitality_wait_staff(request):
#     return render(request, 'dashboard/hospitality_wait_staff.html')

