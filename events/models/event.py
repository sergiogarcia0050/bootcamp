from django.db import models
from courses.models import course
from courses.models import batch
class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.Choices('I', 'P', 'F') # I = Inicial, P = Progreso, F = Finalizacion
    start_date = models.DateField()
    end_date = models.DateField()
    course = models.ForeignKey(course, null=True, on_delete=models.PROTECT)
    batch = models.ForeignKey(batch, null=True, on_delete=models.PROTECT)

    class Meta:
        db_table = 'events'
        verbose_name = 'event'
        verbose_name_plural = 'events'

        constraints = [
            models.CheckConstraint(
                check=models.Q(start_date__lt = models.F('end_date')),
                name='start_date_must_be_less_than_end_date'
            ),
            models.CheckConstraint(
                check=(
                    (models.Q(batch__isnull=False) & models.Q(course__isnull=True)) |
                    (models.Q(batch__isnull=True) & models.Q(course__isnull=False))
                ),
                name='exactly_one_batch_or_bootcamp'
            ),
            models.CheckConstraint(
                check = models.Q(batch__isnull=False) & models.Q(type__in=['I', 'F']),
                name='initial_and_final_events_must_have_batch'
            ),
            models.CheckConstraint(
                check = (models.Q(course__isnull=False) & models.Q(type_in=['I', 'P','F'])),
                name='course_events_can_only_be_initial_progress_or_final'
            )

        ]

    

