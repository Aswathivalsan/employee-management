
#from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
#from empapp.views import  employee_details
from rest_framework.routers import DefaultRouter
from empapp.views import EmployeeViewSet


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('person/',person , name= 'person'),

    #path('employee/', employee_details , name='employee_details'),
    #path('employees/', employee_list.as_view() ,name='employee_lists' ),
    path('', include(router.urls)),

]




