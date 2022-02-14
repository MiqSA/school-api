from rest_framework import serializers
from school.models import Student, Class, Subscription

# Responsible to link the database in json form

class StudentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birthday'] # Data available in API



class ClassSerializer(serializers.ModelSerializer):


    class Meta:
        model = Class
        fields = '__all__'



class SubscriptionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Subscription
        exclude = []



class ListSubscriptionsStudentSerializer(serializers.ModelSerializer):
    class_name = serializers.ReadOnlyField(source='class_name.description')
    period = serializers.SerializerMethodField()


    class Meta:
        model = Subscription
        fields = ['class_name', 'period']

    def get_period(self, obj):
        return obj.get_period_display()



class ListStudentsSubscribersClassSeriliazer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')


    class Meta:
        model = Subscription
        fields = ['student_name']
