from django.shortcuts import render, redirect
from sympy import Si
from . forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here. 

def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('landing_page')
    else:
        user_form = SignUpForm()
    context = {
        'user_form': user_form
    }
    return render(request, 'users/signup.html', context)


