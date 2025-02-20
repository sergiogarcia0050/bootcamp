from django.db import models

from courses.models.batch import Batch
from courses.models.course import Course


class BatchCorse(models.Model):
    id = models.UUIDField(primary_key=True)
    batch = models.ForeignKey(Batch, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    
    