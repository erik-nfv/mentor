import random

class SubjectSet(set):
	ALLOWED = {"Math", "Russian", "English"}

	def __init__(self, iterable=None):
		super().__init__(self)
		if iterable:
			for e in iterable:
				self.add(e)
			
	
	def add(self, subject):
		if subject.name not in self.ALLOWED:
			raise ValueError(f'Unknown subject: {subject}')
		super().add(subject)

class UniversityMember:
	def __init__(self, first_name, last_name=None, age=None):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

class Student(UniversityMember):
	def __init__(self, first_name, subjects=None, last_name=None, age=None):
		super().__init__(first_name, last_name, age)
		self.subjects = SubjectSet(subjects)
		self.grades = {key: [] for key in self.subjects}

	def add_grade(self, subject, grade):
		if subject not in self.subjects:
			raise ValueError(f'Student does not study subject: {subject}')
		self.grades[subject].append(grade)

	def get_grades(self):
		return self.grades
	
	def get_avg_grade(self, subject):
		if subject not in self.subjects:
			raise ValueError(f'Student does not study subject: {subject}')
		if len(self.grades[subject]) == 0:
			return 0
		return sum(self.grades[subject]) / len(self.grades[subject])

class Teacher(UniversityMember):
	def __init__(self, first_name, subjects=None, last_name=None, age=None):
		super().__init__(first_name, last_name, age)
		self.subjects = SubjectSet(subjects)

class Subject:
	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return(self.name)
	
	def start_lesson(self, teacher, students):
		for student in students:
			student.add_grade(self, random.randint(1,5))

m = Subject("Math")
r = Subject("Russian")

s = Student('Petr', (m, r))
t = Teacher('Ivan', (m,))

print(s.subjects)
print(s.grades)
s.add_grade(m, 4)
s.add_grade(m, 5)
print(s.grades)
print(s.get_avg_grade(m))

print(t.subjects)

m.start_lesson(t, (s,))
print(s.grades)