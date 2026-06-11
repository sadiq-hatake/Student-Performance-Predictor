from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    attendance = models.FloatField()

    internal_marks = models.FloatField()

    assignment_score = models.FloatField()

    study_hours = models.FloatField()

    gpa = models.FloatField()

    def __str__(self):
        return self.name