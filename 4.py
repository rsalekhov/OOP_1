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

  #def __lt__(self, other):
      #return (sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())) < (sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values()))

  #def __gt__(self, other):
      #return (sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())) > (sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values()))

  #def __eq__(self, other):
      #return (sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())) == (sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values()))

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'


student_1 = Student('Ruoy', 'Eman', 'male', 'введение в программирование')
student_1.courses_in_progress += ['Python', 'Git']

student_2 = Student('Alice', 'Smith', 'female', 'JavaScript')
student_2.courses_in_progress += ['Python', 'JavaScript']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Eva', 'Green')
reviewer_2.courses_attached += ['Python', 'JavaScript']

lecturer_1 = Lecturer('John', 'Doe')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Jane', 'Doe')
lecturer_2.courses_attached += ['Python', 'JavaScript']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 7)

reviewer_2.rate_hw(student_1, 'JavaScript', 9)
reviewer_2.rate_hw(student_1, 'JavaScript', 8)
reviewer_2.rate_hw(student_2, 'JavaScript', 7)
reviewer_2.rate_hw(student_2, 'JavaScript', 6)

student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_2, 'Python', 7)
student_1.rate_lecture(lecturer_2, 'Python', 6)

student_2.rate_lecture(lecturer_1, 'JavaScript', 9)
student_2.rate_lecture(lecturer_1, 'JavaScript', 8)
student_2.rate_lecture(lecturer_2, 'JavaScript', 7)
student_2.rate_lecture(lecturer_2, 'JavaScript', 6)


print("Информация о студентах:")
print("Студент 1:")
print(student_1)
print("\nСтудент 2:")
print(student_2)
print("\n")

print("Информация о лекторах:")
print("Лектор 1:")
print(lecturer_1)
print("\nЛектор 2:")
print(lecturer_2)
print("\n")
