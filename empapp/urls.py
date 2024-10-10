#from django.contrib import admin
#from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from empapp.views import employee_list



urlpatterns = [
    
   # path('person/',person , name= 'person'),
    path('employee/',employee_list.as_view() ,name='employee_list' ),
   # path('employees/', employee_details , name='employee_details')
]
