from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib import messages
from django.db.models import Avg, Max

from .forms import StudentForm
from .models import Student
from .ml_utils import model,metrics




def home(request):

    predicted_score = None
    suggestion = None

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            student = form.save(commit=False)

            prediction = model.predict([[
                student.attendance,
                student.internal_test_1,
                student.internal_test_2,
                student.assignment_score,
                student.study_hours
            ]])

            student.predicted_score = round(prediction[0], 2)

            student.suggestion = generate_suggestion(student)

            student.save()

            predicted_score = student.predicted_score
            suggestion = student.suggestion

            messages.success(
                request,
                "Prediction generated successfully!"
            )

    else:
        form = StudentForm()

    context = {
        'form': form,
        'predicted_score': predicted_score,
        'suggestion': suggestion
    }

    return render(
        request,
        'predictor/home.html',
        context
    )

def students(request):

    query = request.GET.get('q')

    data = Student.objects.all()

    if query:
        data = data.filter(
            name__icontains=query
        )

    return render(
        request,
        'predictor/students.html',
        {'students': data}
    )


def details(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    return render(
        request,
        'predictor/details.html',
        {'student': student}
    )


def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect('students')


def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            updated_student = form.save(commit=False)

            prediction = model.predict([[
                updated_student.attendance,
                updated_student.internal_test_1,
                updated_student.internal_test_2,
                updated_student.assignment_score,
                updated_student.study_hours
            ]])

            updated_student.predicted_score = round(
                prediction[0],
                2
            )
            updated_student.suggestion = generate_suggestion(
    updated_student
)
            updated_student.save()

            messages.success(
                request,
                'Student updated successfully!'
            )

            return redirect('students')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'predictor/home.html',
        {'form': form}
    )


def dashboard(request):

    total_students = Student.objects.count()

    average_score = Student.objects.aggregate(
        Avg('predicted_score')
    )['predicted_score__avg']

    highest_score = Student.objects.aggregate(
        Max('predicted_score')
    )['predicted_score__max']

    context = {
        'total_students': total_students,
        'average_score': average_score,
        'highest_score': highest_score,

        'r2_score': metrics['r2_score'],
    'mae': metrics['mae'],
    'rmse': metrics['rmse'],

    'feature_importance': metrics['feature_importance']
        
    }

    return render(
        request,
        'predictor/dashboard.html',
        context
    )

def generate_suggestion(student):

    suggestions = []

    if student.attendance < 75:
        suggestions.append(
            "Improve attendance above 75%."
        )

    if student.internal_test_1 < 25:
        suggestions.append(
            "Focus more on Internal Test 1 preparation."
        )

    if student.internal_test_2 < 25:
        suggestions.append(
            "Focus more on Internal Test 2 preparation."
        )

    if student.assignment_score < 7:
        suggestions.append(
            "Submit assignments on time and improve quality."
        )

    if student.study_hours < 3:
        suggestions.append(
            "Increase daily study time to at least 3 hours."
        )

    if student.predicted_score < 60:
        suggestions.append(
            "Consider attending extra classes or seeking guidance."
        )

    if not suggestions:
        return "Excellent performance. Keep up the good work!"

    return " ".join(suggestions)