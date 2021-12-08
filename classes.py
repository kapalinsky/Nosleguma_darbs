# jauna klases izveidošana:


class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def get_average_grade(self):
        summa = sum(self.grades)
        grades_num = len(self.grades)
        average_grade = summa / grades_num
        print(average_grade)


student_1 = Student(
    name='Andris',
    grades=[7, 4, 10]
)


student_1_average_grade = student_1.get_average_grade()
"""
atgriezts skaitlis ir float tipa!
"""
