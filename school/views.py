from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from school.models import Student, Class, Subscription
from school.serializer import StudentSerializer, ClassSerializer, SubscriptionSerializer, \
    ListSubscriptionsStudentSerializer, ListStudentsSubscribersClassSeriliazer



class StudentsViewSet(viewsets.ModelViewSet):
    """ Show all students """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ClassViewSet(viewsets.ModelViewSet):
    """ Show all classes"""

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class SubscriptionViewSet(viewsets.ModelViewSet):
    """ Show all subscriptions"""

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ListSubscriptionStudent(generics.ListAPIView):
    """ Listing subscriptions from students"""

    def get_queryset(self):
        queryset = Subscription.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListSubscriptionsStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListStudentSubscription(generics.ListAPIView):
    """ Listing students from an class"""

    def get_queryset(self):
        queryset = Subscription.objects.filter(class_name_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListStudentsSubscribersClassSeriliazer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
