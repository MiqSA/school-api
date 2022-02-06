from rest_framework import serializers
from school.models import Student, Class

# Responsible to link the database in json form

class StudentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birthday'] # Data available in API



class ClassSerializer(serializers.ModelSerializer):


    class Meta:
        model = Class
        fields = '__all__'



