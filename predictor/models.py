from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

    attendance = models.FloatField()

    internal_test_1 = models.FloatField()

    internal_test_2 = models.FloatField()

    assignment_score = models.FloatField()

    study_hours = models.FloatField()

    predicted_score = models.FloatField(
        null=True,
        blank=True
    )