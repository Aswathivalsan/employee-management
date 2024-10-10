
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import Employee
from.serializers import EmployeeSerializer
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

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def employee_list (request):
    if request.method == 'GET':
        objEmployee = Employee.objects.all() 
        serializer = EmployeeSerializer(objEmployee, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        data = request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=400)
    
    elif request.method == 'PUT':
        data =request.data
        emp_id =data.get('id',None)
        if not emp_id:
            return Response({"error": "Employee ID is required for update."}, status=400)
        try:
           obj = Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        serializer = EmployeeSerializer(obj, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=400)
    

    elif request.method == 'PATCH':
        data = request.data
        emp_id =data.get('id',None)
        if not emp_id:
            return Response({"error": "Employee ID is required for updating an employee."}, status=400)
        try:
            obj = Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        serializer = EmployeeSerializer(obj, data =data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        data = request.data
        emp_id =data.get('id',None)
        if not emp_id:
            return Response({"error": "Employee ID is required for updating an employee."}, status=400)
        try:
            obj = Employee.objects.get(id=emp_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)
        
        obj.delete()
        return Response({'message': "Employee deleted successfully"}, status=204)
