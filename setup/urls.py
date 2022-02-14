"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url, include
from school.views import StudentsViewSet, ClassViewSet, SubscriptionViewSet, ListSubscriptionStudent, ListStudentSubscription
from rest_framework import routers

from setup import settings

# if settings.DEBUG:
router = routers.DefaultRouter()
# else:
# router = routers.SimpleRouter()


# router = routers.DefaultRouter()

router.register(r'students', StudentsViewSet, basename='Students')
router.register('classes', ClassViewSet, basename='Classes')
router.register('subscriptions', SubscriptionViewSet, basename='Subscriptions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), ),
    path('student/<int:pk>/subscriptions/', ListSubscriptionStudent.as_view() ),
    path('class/<int:pk>/subscriptions/', ListStudentSubscription.as_view() ),
    # url(r'v1.0/', include(router.urls)),
]
