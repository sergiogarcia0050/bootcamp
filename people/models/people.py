from django.db import models


class Person(models.Model):
	id = models.UUIDField(primary_key=True, editable=False)
	name = models.CharField(max_length=100)
	

	
	

