from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'attendance',
            'internal_test_1',
            'internal_test_2',
            'assignment_score',
            'study_hours'
        ]