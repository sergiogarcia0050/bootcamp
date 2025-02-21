from rest_framework import serializers
from events.models import Event

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'category', 'start_date', 'end_date', 'course', 'batch']
