from django.db import models


class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_average_grade(self):
        grades_int = list(map(int, self.grades.split(',')))
        summa = sum(grades_int)
        average_grade = summa / len(grades_int)
        return average_grade


class StudentModel(models.Model):
    name = models.CharField(max_length=250)
    grades = models.CharField(max_length=100)
    average_grade = models.FloatField()
