# داخل ملف events/models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name
# داخل ملف events/serializers.py
from rest_framework import serializers
from .models import Event  # تأكد من أنك استوردت النموذج بشكل صحيح

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # يعني أن جميع الحقول في نموذج Event سيتم تضمينها
