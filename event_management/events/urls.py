from django.db import models
from django.urls import include, path
from events.views import EventViewSet  # استيراد EventViewSet من التطبيق events

from event_management.events.views import EventViewSet

router = DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')  # تسجيل viewset

urlpatterns = [
    path('', include(router.urls)),  # تضمين الروابط التي يتم إنشاؤها بواسطة الـ router
]

