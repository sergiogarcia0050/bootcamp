from rest_framework import viewsets
from rest_framework import serializers
from courses.models.course import Course

class CourseSerializar(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializar
    
    