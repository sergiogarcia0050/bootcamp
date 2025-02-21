from rest_framework.test import APITestCase

from courses.models.course import Course
from people.models.people import Person

class CourseTestCase(APITestCase):
    
    def setUp(self):
        self.person = Person.objects.create(name = 'El Joe Arroyo')
        self.course = Course.objects.create(name= 'Salsa', descripcion = "Un gran curso de salsa")
        
    def test_create_course(self):
        
        
    