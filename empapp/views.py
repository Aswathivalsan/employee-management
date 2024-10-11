
from rest_framework.response import Response
from rest_framework. decorators import api_view
from rest_framework.views import APIView
from.models import Employee 
from.serializers import EmployeeSerializer
from rest_framework import status
from rest_framework import viewsets


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

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def employee_list(request):
   
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     # Handle POST request: Create a new employee
#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PUT':
#         try:
#             # Extract the ID of the employee to update from the request
#             employee_id = request.data.get('id')
#             employee = Employee.objects.get(id=employee_id)
#         except Employee.DoesNotExist:
#             return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
   
#     elif request.method == 'PATCH':
#         try:
#             employee_id = request.data.get('id')
#             employee = Employee.objects.get(id=employee_id)
#         except Employee.DoesNotExist:
#             return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = EmployeeSerializer(employee, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     elif request.method == 'DELETE':
#         try:
#             employee_id = request.data.get('id')
#             employee = Employee.objects.get(id=employee_id)
#             employee.delete()
#             return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except Employee.DoesNotExist:
#             return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        #class base

# class employee_list(APIView):
#     def get(self,request):
    
#         employees = Employee.objects.all() 
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK )
    

#     def post(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self,request):
#         employee_id =request.data.get('id')

#         try:
#             employees = Employee.objects.get(id=employee_id)
#         except Employee.DoesNotExist:
#                     return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = EmployeeSerializer(employees, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def patch(self, request):
#         employee_id = request.data.get('id')
#         try:
#             employee = Employee.objects.get(id=employee_id)
#         except Employee.DoesNotExist:
#             return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = EmployeeSerializer(employee, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request):
#         employee_id = request.data.get('id')
#         if not employee_id:
#             return Response({"error": "Employee ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             employees = Employee.objects.get(id=employee_id)
#         except Employee.DoesNotExist:
#             return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         employees.delete()
#         return Response({"message": "Employee deleted successfully"}, status=status.HTTP_200_OK)
    



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        employee_id = kwargs.get('pk')
        try:
            employee = self.get_object()
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        employee_id = kwargs.get('pk')
        try:
            employee = self.get_object()
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        employee_id = kwargs.get('pk')
        try:
            employee = self.get_object()
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)