import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class PersonUserManager(BaseUserManager):
	def create_user(self, email, name, password=None, **extra_fields):
		if(not email):

			raise ValueError('Es necesario un correo para registarse')
		email = self.normalize_email(email)
		name = self.name
		user = self.model(email = email, name = name , **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user
class Person(AbstractUser):
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=100)
	email = models.TextField(max_length=100, unique=True)


	REQUIRED_FIELDS = []
	USERNAME_FIELD = "email"
	objects =  PersonUserManager()


	def __str__(self):
		return self.email

	class Meta:
		db_table = 'person'
		verbose_name = 'person'	
		verbose_name_plural = 'persons'

