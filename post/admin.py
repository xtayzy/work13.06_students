from turtledemo.sorting_animate import Block

from django.contrib import admin

# Register your models here.

from post.models import Category, Course, StudentCard, Student

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(StudentCard)
admin.site.register(Student)
