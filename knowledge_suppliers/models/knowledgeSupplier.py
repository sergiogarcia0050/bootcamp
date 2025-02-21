import uuid
from django.db import models

from courses.models.course import Course

class KnowledgeSupplier(models.Models):
	id = models.UUIDField(primary_key = True, default=uuid.uuid4)
	name = models.TextField(max_length = 100, unique = True)
	addres = models.TextField(max_length = 100)
	course_id = models.ForeignKey(Course, on_delete=models.PROTECT)


	class Meta:
		db_table = 'knowledge_supplier'
		verbose_name = 'knowledge_sipplier'	
		verbose_name_plural = 'knowledge_sippliers'



	

	
