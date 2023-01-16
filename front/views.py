from django.shortcuts import render, redirect
from . forms import DataForm
from .models import Data
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    return render(request, 'front/landing_page.html')

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('results_page')

    else:
        form = DataForm()

    context = {
        'form': form
        }
    return render(request, 'front/index.html', context)

@login_required(login_url='login')
def results_page(request):
    results = Data.objects.all()
    context = {
        'results':results
    }
    return render(request, 'predictions/prediction_result.html', context)
    
@login_required(login_url='login')
def visualizations(request):
    return render(request, 'predictions/visualizations.html')