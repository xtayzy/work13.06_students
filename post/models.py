from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')


class StudentCard(models.Model):
    card_id = models.IntegerField(unique=True)

 
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    courses = models.ManyToManyField('Course', related_name='students')
    card = models.OneToOneField(StudentCard, on_delete=models.CASCADE)

