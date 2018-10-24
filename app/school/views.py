from django.shortcuts import render

from .models import School, Student


def index(request):
    return render(request, 'index.html')


def school_list(request):
    schools = School.objects.all()
    context = {
        'schools': schools,
    }
    return render(request, 'school_list.html', context)


def school_detail(request, school_id):
    school = School.objects.get(pk=school_id)
    students = school.student_set.all()
    context = {
        'school': school,
        'students': students,
    }
    return render(request, 'school_detail.html', context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student_list.html', context)


def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    friends = student.friends.all()
    school = student.school
    context = {
        'student': student,
        'friends': friends,
        'school': school,
    }
    return render(request, 'student_detail.html', context)
