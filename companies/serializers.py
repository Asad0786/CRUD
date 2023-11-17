from .models import Company, Employee, models
from rest_framework import serializers 

class CompanySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['id','name', 'location', 'type','active','contact','description','registered_at']

    def create(self, validated_data):
        print(validated_data['type'])
        company_db_item = Company(name = validated_data['name'],
                                  location =validated_data['location'], type = validated_data['type'],
                                  active = validated_data['active'],contact = validated_data['contact'],
                                  description= validated_data['description'])
       
        company_db_item.save()
        return company_db_item
    
    def update(self, instance, validated_data):
        instance.name = f"{validated_data['name']}"
        instance.location = validated_data['location']
        instance.type = validated_data['type']
        instance.active = validated_data['active']
        instance.contact = validated_data['contact']
        instance.description = validated_data['description']

        instance.save()
        return instance
    
    def patch(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location',instance.location)
        instance.type = validated_data.get('type',instance.type)
        instance.active = validated_data.get('active', instance.active)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.description = validated_data.get('description', instance.description)
        
        instance.save()
        return instance
    
    def listAll(self, queryset):
        required_data={}
        
        for x in queryset:
            required_data.update({x.__dict__['id']:x.__dict__['name']})

        print(required_data)
        return required_data
    
    def retrieve(self, instance):
        if(instance.active):
            return instance.name + " - " + "Active"
        else:
            return instance.name + " - " + "In Active"
        
    def delete(self, instance):
        try:
            instance.delete()
        except Exception as e:
            print (e)
        
        return True

    
class DefaultSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(many=True)
    class Meta:
        model = Company
        fields = ['employee']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CustomEmployeeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = ['id','name','emp_type','active','salary', 'emp_id','company']

    