from django import forms
from . models import Data


class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = ['county', 'population', 'max_temp','min_temp','humidity','rainfall','precipitation', 'fishing']

        labels = {
            'max_temp':'Maximum Temprature(degrees)',
            'min_temp': 'Minimum Temprature(degrees)',
            'humidity' : 'Humidity(%)',
            'rainfall': 'Rainfall(mm)',
            'precipitation' : 'Precipitation(%)',
        }
