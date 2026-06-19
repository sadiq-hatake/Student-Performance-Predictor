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

        widgets = {
            'attendance': forms.NumberInput(attrs={
                'min': 0,
                'max': 100
            }),
            'internal_test_1': forms.NumberInput(attrs={
                'min': 0,
                'max': 40
            }),
            'internal_test_2': forms.NumberInput(attrs={
                'min': 0,
                'max': 40
            }),
            'assignment_score': forms.NumberInput(attrs={
                'min': 0,
                'max': 10
            }),
            'study_hours': forms.NumberInput(attrs={
                'min': 0,
                'max': 24
            }),
        }