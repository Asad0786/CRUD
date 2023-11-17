from .serializers import CompanySerializer, DefaultSerializer, CustomEmployeeSerializer
from rest_framework import status, mixins, viewsets, generics
from rest_framework.response import Response

from .models import Company, Employee


class DefaultComapnyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = DefaultSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = CustomEmployeeSerializer

# http://localhost:8000/company/new
class CustomCompanyViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset  = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwags):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        company_db_item = serializer.create(serializer.validated_data)
        print(company_db_item)
        return Response(CompanySerializer(company_db_item).data,status=201)
    
    def update(self, request, *args, **kwags):
        instance =self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_company_db_item = serializer.update(instance, serializer.validated_data)
        return Response(CompanySerializer(updated_company_db_item).data,status=201)

    def partial_update(self, request, *args, **kwargs):
        instance =self.get_object()
        serializer = self.get_serializer(data=request.data, partial =True)
        serializer.is_valid(raise_exception=True)
        patched_comapny_db_item = serializer.patch(instance, serializer.validated_data)
        return Response(CompanySerializer(patched_comapny_db_item).data, status=201)
    
    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer()
        requested_data = serializer.listAll(queryset)
        return Response(requested_data, status=201)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        company = serializer.retrieve(instance)
        return Response(company, status=201)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer()
        if(serializer.delete(instance)):
            return Response("Deleted", status=201)
        else:
            return Response("Error encountered", status=500)
        

        