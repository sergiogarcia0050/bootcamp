from rest_framework import viewsets
from events.serializers.events import EventsSerializer
from events.models.event import Event

class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    queryset = Event.objects.all()