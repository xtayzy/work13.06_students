from django.urls import path
from post import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.cats, name='cats'),
    path('category-page/<int:id>', views.cat_page, name='cat_page'),
    path('delete-category/<int:id>', views.delete_cat, name='delete_cat'),
    path('courses/', views.courses, name='courses'),
    path('course-page/<int:id>', views.course_page, name='course_page'),
    path('delete-course/<int:id>', views.delete_course, name='delete_course'),
    path('students/', views.students, name='students'),
    path('student-page/<int:id>', views.student, name='student'),
    path('delete-student/<int:id>', views.delete_student, name='delete_student'),
    path('add-card', views.add_card, name='add_card'),
]

