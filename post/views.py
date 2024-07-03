from django.shortcuts import render, redirect

from post.forms import CategoryForm, CourseForm, StudentForm, StudentCardForm
from post.models import Category, Course, Student


# Create your views here.


def index(request):

    ctx = {
        'categories': Category.objects.all(),
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
    }

    return render(request, 'post/index.html', ctx)


def cats(request):
    cats = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'categories': cats,
        'form': CategoryForm(),
    }

    return render(request, 'post/cats_page.html', ctx)


def cat_page(request, id):
    cat = Category.objects.get(pk=id)
    courses = cat.courses.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()

    ctx = {
        'cat': cat,
        'form': CategoryForm(),
        'courses': courses,
    }

    return render(request, 'post/cat_page.html', ctx)


def delete_cat(request, id):
    cat = Category.objects.get(pk=id)
    cat.delete()

    return redirect('cats')


def courses(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'courses': courses,
        'form': CourseForm(),
    }

    return render(request, 'post/courses_page.html', ctx)


def course_page(request, id):
    course = Course.objects.get(pk=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()

    ctx = {
        'course': course,
        'form': CourseForm(),
        'students': course.students.all(),
    }

    return render(request, 'post/course_page.html', ctx)


def delete_course(request, id):
    course = Course.objects.get(pk=id)
    course.delete()

    return redirect('courses')


def students(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    ctx = {
        'students': students,
        'form': StudentForm(),
        'cards_form': StudentCardForm(),
    }

    return render(request, 'post/students_page.html', ctx)


def student(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

    ctx = {
        'student': student,
        'form': StudentForm(),
        'courses': student.courses.all(),
    }

    return render(request, 'post/student_page.html', ctx)


def delete_student(request, id):
    student = Student.objects.get(pk=id)
    student.delete()

    return redirect('students')


def add_card(request):
    if request.method == 'POST':
        form = StudentCardForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('students')