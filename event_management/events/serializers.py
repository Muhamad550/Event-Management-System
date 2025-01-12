from django.db import models

from api_project.api import serializers
from event_management import events

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = events.models.Event
        fields = '__all__'
