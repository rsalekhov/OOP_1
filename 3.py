class Student:
  def __init__(self, name, surname, gender, finished_courses):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = [finished_courses]
      self.courses_in_progress = []
      self.grades = {}

  def rate_lecture(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self):
      average_grade = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
      courses_in_progress = ', '.join(self.courses_in_progress)
      finished_courses = ', '.join(self.finished_courses)
      return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
              f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
              f"Курсы в процессе изучения: {courses_in_progress}\n"
              f"Завершенные курсы: {finished_courses}")

class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}

  def __str__(self):
      average_grade = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
      return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}")

  def __lt__(self, other):
      return (sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())) < (sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values()))

  def __gt__(self, other):
      return (sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())) > (sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values()))

  def __eq__(self, other):
      return (sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())) == (sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values()))

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender', 'введение в программирование')
best_student.courses_in_progress += ['Python, Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python, Git']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python, Git']

cool_reviewer.rate_hw(best_student, 'Python, Git', 10)
cool_reviewer.rate_hw(best_student, 'Python, Git', 10)
cool_reviewer.rate_hw(best_student, 'Python, Git', 10)

best_student.rate_lecture(cool_lecturer, 'Python, Git', 8)
best_student.rate_lecture(cool_lecturer, 'Python, Git', 9)
best_student.rate_lecture(cool_lecturer, 'Python, Git', 7)

print("Оценки студента за 'Python, Git':", best_student.grades.get('Python, Git', []))
print("Оценки лектора за 'Python, Git':", cool_lecturer.grades.get('Python, Git', []))

print("\n")
print("Студент:")
print(best_student)
print("\n")
print("Лектор:")
print(cool_lecturer)
print("\n")
print("Сравнение студента и лектора:")
if best_student > cool_lecturer:
    print("Студент лучше лектора")
elif best_student < cool_lecturer:
    print("Лектор лучше студента")
else:
    print("Студент и лектор равны по оценкам")
