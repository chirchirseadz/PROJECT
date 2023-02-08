from ast import If
from distutils.log import FATAL
from django.shortcuts import render, redirect
from .forms import EmployeeProfileUpdateForm, EmployerProfileUpdateForm
from .forms import UserSignUpForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction


# Create your views here. 



# Admin Registration Process

@transaction.atomic
def admin_signup(request):
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_admin = True
            user.save()
            return redirect('user-dashboard')
    else:
        user_form = UserSignUpForm()
        
    context = {
        'form': user_form,
    }
    return render(request, 'users/admin_signup.html', context)


# Employer Registration Process
@transaction.atomic
def employer_signup(request):
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_employer = True
            user.save()
           
            return redirect('user-dashboard')
    else:
        user_form = UserSignUpForm()
        
    context = {
        'user_form': user_form,
    }
    return render(request, 'users/employer_signup.html', context)

#  Employee registration process
def employee_signup(request):
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_applicant = True
            user.save()
            return redirect('user-dashboard')
    else:
        user_form = UserSignUpForm()
        
    context = {
        'user_form': user_form,
    }
    return render(request, 'users/employee_signup.html', context)



@login_required(login_url='login')
def profile(request):
    return render(request, 'users/profile.html')


@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        employee_profile_update_form = EmployeeProfileUpdateForm(request.POST, request.FILES, instance = request.user.user_profile)
        
        if user_update_form.is_valid() and employee_profile_update_form.is_valid():
            user_update_form.save()
            employee_profile_update_form.save()
            profile_updated = employee_profile_update_form.cleaned_data.get("profile_update")
            if profile_updated == False:
                 messages.error(request, 'Kindly check the update profile checkbox')
            else:
                messages.success(request, 'Profile Updated Successfully !!')
                return redirect('user_profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        employee_profile_update_form = EmployeeProfileUpdateForm(instance=request.user.user_profile)
        
       
    context = {
        'user_update_form': user_update_form,
        'employee_profile_update_form': employee_profile_update_form,
        
    }
    return render(request, 'users/profile_update.html', context)

def employer_profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        employer_profile_update_form = EmployerProfileUpdateForm(request.POST, request.FILES, instance = request.user.user_profile)
        if employer_profile_update_form.is_valid() and user_update_form.is_valid():
            user_update_form.save()
            employer_profile_update_form.save()
            profile_updated = employer_profile_update_form.cleaned_data.get("profile_updated")

            if profile_updated == True:
                messages.success(request, 'Profile Updated Successfully !!')
                return redirect('user_profile')
            else:
                messages.error(request, 'Kindly check the update completed checkbox since your Request will not be attended to !! ')
                return redirect('employer_profile_update')
                
            # return redirect('user_profile')
    else:
        employer_profile_update_form = EmployerProfileUpdateForm(instance = request.user.user_profile)
        user_update_form = UserUpdateForm(instance=request.user)
    context = {
        'employer_profile_update_form':employer_profile_update_form,
        'user_update_form': user_update_form
    }
    return render(request, 'users/profile_update.html', context)





    