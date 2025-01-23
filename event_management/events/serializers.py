from django.db import models

from api_project.api import serializers
from event_management import events
from event_management.utils.validators import validate_event_date

def create_event(request):
    event_date = request.data.get('date')
    validate_event_date(event_date)  # سيتم رفع خطأ إذا كان التاريخ في الماضي
    # أكمل إنشاء الفعالية...

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = events.models.Event
        fields = '__all__'
