import random
from enum import StrEnum

class SubjectEnum(StrEnum):
    # +Для заранее известного списка констант удобно использовать StrEnum, почитай его отличие от обычного Enum
    MATH = "Math"
    RUSSIAN = "Russian"
    ENGLISH = "English"

class UniversityMember:
    def __init__(self, first_name, last_name=None, age=None, subjects=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.subjects = UniversityMember._validate_subjects(subjects)

    @staticmethod
    def _validate_subjects(subjects):
        if subjects is None:
            return set()
        for subj in subjects:
            if not isinstance(subj, Subject):
                print(type(subj))
                raise ValueError(f'Subject is not allowed: {subj}')
        return set(subjects)

class Student(UniversityMember):
    def __init__(self, first_name, last_name=None, age=None, subjects=None):
        super().__init__(first_name, last_name, age, subjects)
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
    def __init__(self, first_name, last_name=None, age=None, subjects=None):
        super().__init__(first_name, last_name, age, subjects)
    # У учителя хотелось бы видеть логику какую-то
    # +А почему если поле subject есть и у учителя и у студента - оно не в базовом классе?

class Subject:
    def __init__(self, name: SubjectEnum):
        if not isinstance(name, SubjectEnum):
            raise ValueError(f'Subject is not allowed: {name}')
        self.name = name
    def __repr__(self):
        return self.name
    # +Зачем здесь скобки? форматируй код согласно PEP8 (ctrl + alt + l в pycharm)

    def __eq__(self, other):
        return isinstance(other, Subject) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def start_lesson(self, teacher, students):
        if self not in teacher.subjects:
            raise ValueError(f'Teacher does not teach subject: {self}')
        for student in students:
            if self not in student.subjects:
                raise ValueError(f'Student does not study subject: {self}')
            student.add_grade(self, random.randint(1,5))
            # Границы оценок лучше вынести в константы в тело класса, а не хардкодить вот так в коде
            # К ним будет удобно потом повязываться другим кодом чтобы генерировать тестовые данные или проверять что-то

# Советую для генерации тестовых данных использовать Faker
m = Subject(SubjectEnum.MATH)
r = Subject(SubjectEnum.RUSSIAN)

m2 = Subject(SubjectEnum.MATH)

s = Student('Petr', subjects=(m, r, m2))
t = Teacher('Ivan', subjects=(m,))

print(s.subjects)
print(s.grades)
s.add_grade(m, 4)
s.add_grade(m, 5)
print(s.grades)
print(s.get_avg_grade(m))

print(t.subjects)

# m.start_lesson(t, (s,))
# print(s.grades)

# Ошибка
# b = Subject("Biology")
# b.start_lesson(t, (s,))

# Ошибка
# s2 = Student('Petr', (r,))
# m.start_lesson(t, (s2,))