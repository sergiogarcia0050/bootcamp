from rest_framework import viewsets
from rest_framework import serializers
from people.models.people import Person

class PersonSerializar(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializar
