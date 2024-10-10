#from django.contrib import admin
#from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from empapp.views import employee_list, employee_details



urlpatterns = [
    
   # path('person/',person , name= 'person'),
    path('employee/',employee_list ,name='employee_list' ),
    path('employees/', employee_details , name='employee_details')
]
