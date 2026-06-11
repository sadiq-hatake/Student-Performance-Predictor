from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'attendance',
            'internal_marks',
            'assignment_score',
            'study_hours',
            'gpa'
        ]