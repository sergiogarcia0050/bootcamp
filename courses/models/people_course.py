from django.db import models

from courses.models.course import Course

class PeopleCourse(models.Model):
    id = models.UUIDField(primary_key=True)
    people = models.ForeignKey(People, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)