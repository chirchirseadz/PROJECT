from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('user/index/', views.index, name='user-dashboard'),
    path('user/list/', views.list_of_users, name='list_of_users'),
    path('edit/user/<int:id>/', views.edit_user, name='edit_user'),
    # path('user/edit/<int:pk>/', views.edit_user, name='edit_user'),


    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('news_and_notices/', views.news_and_notices, name='news_and_notices'),
    
   
    
    
    
]
