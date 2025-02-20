from django.db import models

from courses.models.course import Course

class KnowledgeSupplier(models.Models):
	id = models.UUIDField(primary_key = True)
	name = models.TextField(max_length = 100)
	addres = models.TextField(max_length = 100)
	course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
