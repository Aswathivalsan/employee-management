
from rest_framework.response import Response
from rest_framework. decorators import api_view
from rest_framework.views import APIView
from.models import Employee
from.serializers import EmployeeSerializer
from rest_framework import status
#@api_view(['GET']) 
#def person(Request):
 #   if Request.method == 'GET':
   #     person_details ={
      # }
       # return  Response(person_details)

@api_view(['GET'])
def employee_details(request):
    if request.method == 'GET':
        empls ={
            "emp_id": "E001",
            "name": "anju",
            "department": "UI UX",
            "salary":15000
        }
        return  Response(empls)

class employee_list(APIView):
    def get(self,request):
    
        employees = Employee.objects.all() 
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK )
    

    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request):
        emp_id =request.data.get('id')

        try:
            employees = Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
                    return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request):
        emp_id = request.data.get('id')
        try:
            employee = Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        emp_id = request.data.get('id')
        if not emp_id:
            return Response({"error": "Employee ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            employees = Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_200_OK)
