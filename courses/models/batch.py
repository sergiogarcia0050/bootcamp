from django.db import models


class Batch(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField()
    