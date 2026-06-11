from django.shortcuts import redirect, render
from .forms import StudentForm
from django.contrib import messages
from .models import Student

def home(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
    else:
        form = StudentForm()

    return render(
        request,
        'predictor/home.html',
        {'form': form}
    )

def students(request):

    data = Student.objects.all()

    return render(
        request,
        'predictor/students.html',
        {'students': data}
    )

def details(request, id):

    student = Student.objects.get(id=id)

    return render(
        request,
        'predictor/details.html',
        {'student': student}
    )


def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('students')