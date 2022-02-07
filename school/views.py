from rest_framework import viewsets, permissions
from school.models import Student, Class, Subscription
from school.serializer import StudentSerializer, ClassSerializer, SubscriptionSerializer



class StudentsViewSet(viewsets.ModelViewSet):
    """ Show all students """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]



class ClassViewSet(viewsets.ModelViewSet):
    """ Show all classes"""

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    # permission_classes = [permissions.IsAuthenticated]



class SubscriptionViewSet(viewsets.ModelViewSet):
    """ Show all subscriptions"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    # permission_classes = [permissions.IsAuthenticated]
