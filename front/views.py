from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import DataForm
from .models import Data
from django.contrib.auth.decorators import login_required


# algorithm dependencies
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection  import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib

# Create your views here.



def landing_page(request):
    return render(request, 'front/landing_page.html')


@login_required(login_url='landing_page')

def index(request):
    form = DataForm(request.POST)
    # model= joblib.load('hunger_prediction.joblib')
    data = pd.read_csv("hunger.csv")

    x = data.drop(columns=['Area_square_km','outcome', 'county'], axis=1)
    
    scaler = StandardScaler()
    scaler.fit(x)

    standard_data = scaler.transform(x)


    X = standard_data
    y = data['outcome']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=2)

    classifier = svm.SVC(kernel='linear')
    classifier.fit(x_train, y_train)

    x_train_predictions = classifier.predict(x_train)

    trainning_data_accuracy = accuracy_score(x_train_predictions, y_train)

    if request.method == 'POST':        
        if form.is_valid():
            data_form = form.save(commit=False)
            data_list = []
            data_list.append(request.POST['population'])
            data_list.append(request.POST['max_temp'])
            data_list.append(request.POST['min_temp'])
            data_list.append(request.POST['humidity'])
            data_list.append(request.POST['rainfall'])
            data_list.append(request.POST['precipitation'])
            data_list.append(request.POST['fishing'])

                    
            # changing the inputs to numpy data_array
            input_data_as_numpy_array = np.asanyarray(data_list)

            # Reshape data in the array since we are predicting data of only one instance
            reshaped_data = input_data_as_numpy_array.reshape(1, -1)

            #  Standardize the input data
            std_data = scaler.transform(reshaped_data)

            results = classifier.predict(std_data)

            data_form.results = results
            accuracy = trainning_data_accuracy * 100

            data_form.accuracy = accuracy

            data_form.save()
            return redirect('results_page')

    else:
        form = DataForm()
        results = ''
        
    context = {
        'results': results,
        'form': form
    }
    
    return render(request, 'front/index.html', context)

@login_required(login_url='landing_page')
def results_page(request):
    results = Data.objects.all()
    result_count = results.count()
    context = {
        'results':results,
        'result_count': result_count,
    }
    return render(request, 'predictions/prediction_result.html', context)
    
@login_required(login_url='landing_page')
def visualizations(request):
    return render(request, 'predictions/visualizations.html')