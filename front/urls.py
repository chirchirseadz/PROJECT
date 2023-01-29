from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='index_page'),
    path('landing', views.landing_page, name='landing_page'),
    path('predictions/results', views.results_page, name='results_page'),
    path('visualizations/', views.visualizations, name='visualizations'),
   
]
