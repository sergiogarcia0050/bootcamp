from django.db import models

class Course(models.Model):
    
    id = models.UUIDField(primary_key=True)
    title = models.CharField()
    description = models.TextField()
    
    
    
    