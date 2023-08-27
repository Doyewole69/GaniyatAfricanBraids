from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'booking'

urlpatterns = [
    path('book/', views.book, name='book'),
    path('contact/',views.contact , name='contact'),
    path('success/',views.success , name='success'),
    path('service/',views.services , name='service'),
    path('thankyou/',views.thankyou , name='thankyou'),
     path('extrasmallknotless/',views.extrasmallknotless , name='extrasmallknotless'),
    
    
    

]