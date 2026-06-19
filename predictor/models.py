from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):

    name = models.CharField(max_length=100)

    attendance = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    internal_test_1 = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(40)
        ]
    )

    internal_test_2 = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(40)
        ]
    )

    assignment_score = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    study_hours = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(24)
        ]
    )

    predicted_score = models.FloatField(
        null=True,
        blank=True
    )

    suggestion = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name