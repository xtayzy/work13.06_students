from django import forms

from post.models import Category, Course, StudentCard, Student


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class StudentCardForm(forms.ModelForm):
    class Meta:
        model = StudentCard
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'