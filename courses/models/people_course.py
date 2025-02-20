from django.db import models

from courses.models.course import Course
from people.models.people import Person

class PeopleCourse(models.Model):
    id = models.UUIDField(primary_key=True)
    people = models.ForeignKey(Person, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)