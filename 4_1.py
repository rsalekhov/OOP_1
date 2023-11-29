class Student:
  def __init__(self, name, grades):
      self.name = name
      self.grades = grades

class Lecturer:
  def __init__(self, name, grades):
      self.name = name
      self.grades = grades



def avg_student_grade_by_course(students, course):
  total_grades = 0
  count = 0
  for student in students:
      if course in student.grades:
          total_grades += sum(student.grades[course])
          count += len(student.grades[course])

  if count != 0:
      return total_grades / count
  else:
      return 0

def avg_lecturer_grade_by_course(lecturers, course):
  total_grades = 0
  count = 0
  for lecturer in lecturers:
      if course in lecturer.grades:
          total_grades += sum(lecturer.grades[course])
          count += len(lecturer.grades[course])

  if count != 0:
      return total_grades / count
  else:
      return 0

student_1 = Student('Alice', {'Python': [8, 7]})
student_2 = Student('Bob', {'Python': [7, 6]})
lecturer_1 = Lecturer('John', {'JavaScript': [7, 8]})
lecturer_2 = Lecturer('Jane', {'JavaScript': [8, 9]})

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

avg_student_python = avg_student_grade_by_course(students, 'Python')
print(f"Средняя оценка студентов по курсу Python: {avg_student_python:.2f}")
avg_lecturer_js = avg_lecturer_grade_by_course(lecturers, 'JavaScript')
print(f"Средняя оценка лекторов по курсу JavaScript: {avg_lecturer_js:.2f}")
