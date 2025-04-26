
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Student
from django.contrib import messages

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'schools/course_list.html', {'courses': courses})

@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = Student.objects.filter(course=course)
    return render(request, 'schools/course_detail.html', {
        'course': course,
        'students': students
    })

@login_required
def course_create(request):
    churches = Church.objects.all()
    if request.method == 'POST':
        course = Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            church_id=request.POST['church'],
            instructor_id=request.POST['instructor'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
        )
        messages.success(request, 'Curso criado com sucesso!')
        return redirect('schools:course_detail', pk=course.pk)
    return render(request, 'schools/course_form.html')

@login_required
def student_enroll(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    if request.method == 'POST':
        Student.objects.create(
            person_id=request.POST['person'],
            course=course
        )
        messages.success(request, 'Aluno matriculado com sucesso!')
        return redirect('schools:course_detail', pk=course_pk)
    return render(request, 'schools/student_enroll.html', {'course': course})
