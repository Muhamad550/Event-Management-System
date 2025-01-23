from django.db import models
from django.urls import include, path
from events.views import EventViewSet  # استيراد EventViewSet من التطبيق eventsfrom django.urls import path
from .api.views import EventList, EventDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

from event_management.events.views import EventViewSet

router = DefaultRouter()
router.register('events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')  # تسجيل viewset

urlpatterns = [
    path('', include(router.urls)),  # تضمين الروابط التي يتم إنشاؤها بواسطة الـ router
]


urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
]

