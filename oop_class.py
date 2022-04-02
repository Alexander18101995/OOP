class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecrurer_grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)


class Lecturer(Mentor):
    def __init__ (self,name,last_name):
        self.name = name
        self.last_name = last_name 
        self.sdtudent_lecturer_cours = []


lecturer_grades = {'Git': 10, 'Git': 9, 'Git': 8, 'Git': 7, 'Git': 6,
                   'Git': 5, 'Git': 4, 'Git': 3, 'Git': 2, 'Git': 1}

lecturer_grades = {'Python': 10, 'Python': 9, 'Python': 8, 'Python': 7,
                   'Python': 6,'Python': 5,'Python': 4, 'Python': 3,
                   'Python': 2, 'Python': 1}  


class Reviewe(Mentor):
    def __init__ (self,name,last_name):
        self.name = name
        self.last_name = last_name
        self.studenr_grades
