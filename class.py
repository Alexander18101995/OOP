grades_lecturer_git = [5, 4, 5, 3]
grades_lecturer_python = [5, 4, 3, 4]
grades_student_git = [5, 4, 2, 3]
grades_student_python = [4, 2, 3, 2]
courses = ('Git','Python')
cool_mentor = ('Some', 'Buddy')
best_student = ('Ruoy', 'Eman')
def avg_grades_lecturer_git(grades):
      sum_ = 0
      for git in grades:
        sum_ =+ sum(grades) / len(grades)
        return round(sum(grades) / len(grades), 2)
def avg_grades_lecturer_python(grades):
      sum_ = 0
      for python in grades:
        sum_ =+ sum(grades) / len(grades)
        return round(sum(grades) / len(grades), 2) 
def avg_grades(grades_git,grades_python):
  grades= (grades_git + grades_python) / 2
  return grades
def avg_grades_student_git(grades):
      sum_ = 0
      for git in grades:
        sum_ =+ sum(grades) / len(grades)
        return round(sum(grades) / len(grades), 2)
def avg_grades_student_python(grades):
      sum_ = 0
      for python in grades:
        sum_ =+ sum(grades) / len(grades)
        return round(sum(grades) / len(grades), 2) 
def avg_grades(grades_git,grades_python):
  grades= (grades_git + grades_python) / 2
  return grades
class Student:
    def __init__(self, name, surname, avg_grades):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.avg_grades = avg_grades
        self.lecrurer_grades = []

    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grades}\nКурсы в процессе изучения: {courses[0]}, {courses[1]}\nЗавершенные курсы: Введение в программирование '

    def __lt__(self, other):
      return self.avg_grades < other.avg_grades

some_student = Student(best_student[0],best_student[1],avg_grades(avg_grades_student_git(grades_student_git),avg_grades_student_python(grades_student_python)))
class Lecturer:
    def __init__ (self,name,last_name,avg_grades):
        self.name = name
        self.last_name = last_name 
        self.avg_grades = avg_grades
    def __str__(self):
      return f'Имя: {self.name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: { self.avg_grades }'
some_lecturer = Lecturer(cool_mentor[0],cool_mentor[1],avg_grades(avg_grades_lecturer_git(grades_lecturer_git),avg_grades_lecturer_python(grades_lecturer_python)))
def __lt__(self, other):
  return self.avg_grades < other.avg_grades

print()
print(some_lecturer)
print()
print(some_student)
print(some_student < some_lecturer )