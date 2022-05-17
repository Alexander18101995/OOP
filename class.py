grades_git = [5, 4, 3, 2]
grades_python = [5, 4, 3, 2]
courses = ('Git','Python')
cool_mentor = ('Some', 'Buddy')
best_student = ('Ruoy', 'Eman')
def avg_grades_git(grades):
      sum_ = 0
      for git in grades:
        sum_ =+ sum(grades) / len(grades)
        return round(sum(grades) / len(grades), 0)
def avg_grades_python(grades):
      sum_ = 0
      for python in grades:
        sum_ =+ sum(grades) / len(grades)
        return round(sum(grades) / len(grades), 0)        
def avg_grades(grades_git,grades_python):
  grades= (grades_git + grades_python) / 2
  return grades

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []
        self.lecrurer_grades = []

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grades(avg_grades_git(grades_git),avg_grades_git(grades_python))}\nКурсы в процессе изучения: {courses[0]}, {courses[1]}\nЗавершенные курсы: Введение в программирование '



some_student = Student(best_student[0],best_student[1])
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}'
name_mentor = Mentor(cool_mentor[0],cool_mentor[1])
class Lecturer:
    def __init__ (self,name,last_name):
        self.name = name
        self.last_name = last_name 
    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: {avg_grades(avg_grades_git(grades_git),avg_grades_git(grades_python))}'
some_lecturer = Lecturer(cool_mentor[0],cool_mentor[1])
class Reviewe(Mentor):
    def __init__ (self,name,last_name):
        self.name = name
        self.last_name = last_name
        self.student_grades

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}'
some_reviewe = Mentor(cool_mentor[0],cool_mentor[1])

print(some_reviewe)
print()
print(some_lecturer)
print()
print(some_student)