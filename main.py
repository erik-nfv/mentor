import random
from enum import StrEnum
from faker import Faker


class SubjectEnum(StrEnum):
    MATH = "Math"
    RUSSIAN = "Russian"
    ENGLISH = "English"


class UniversityMember:
    def __init__(self, first_name, last_name=None, age=None, subjects=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.subjects = self._validate_subjects(subjects)

    @staticmethod
    def _validate_subjects(subjects):
        if subjects is None:
            return set()
        for subj in subjects:
            if not isinstance(subj, Subject):
                raise ValueError(f'Subject is not allowed: {subj}')
        return set(subjects)

    def __repr__(self):
        return f"{type(self).__name__} - {self.first_name} {self.last_name or ''}"


class Student(UniversityMember):
    def __init__(self, first_name, last_name=None, age=None, subjects=None, group=None):
        super().__init__(first_name, last_name, age, subjects)
        self.grades = {key: [] for key in self.subjects}
        self.group = group

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f'Student does not study subject: {subject}')
        self.grades[subject].append(grade)

    def do_ticket(self, ticket):
        result = 0
        for question in ticket.qa_dict:
            result += random.randint(0, 1)
        self.add_grade(ticket.subject, result)

    def get_grades(self):
        return self.grades

    def get_avg_grade(self, subject):
        if subject not in self.subjects:
            raise ValueError(f'Student does not study subject: {subject}')
        if len(self.grades[subject]) == 0:
            return 0
        return sum(self.grades[subject]) / len(self.grades[subject])


class Teacher(UniversityMember):
    def __init__(self, first_name, last_name=None, age=None, subjects=None, students=None):
        super().__init__(first_name, last_name, age, subjects)
        if students is None:
            students = set()
        self.students = students

    def add_student(self, student: Student):
        self.students.add(student)


class StudentGroup:
    def __init__(self, name, students=None):
        self.name = name
        self.students = []
        if students is not None:
            for student in students:
                self.append(student)

    def append(self, student):
        self.students.append(student)
        student.group = self.name

    def delete(self, student):
        self.students.remove(student)
        student.group = None

    def __contains__(self, student):
        return student in self.students

    def __len__(self):
        return len(self.students)

    def __eq__(self, other):
        return isinstance(other, StudentGroup) and len(self.students) == len(other.students)

    def __str__(self):
        return str(self.students)

    def __iter__(self):
        return iter(self.students)


class Subject:
    MIN_GRADE = 1
    MAX_GRADE = 5

    def __init__(self, name: SubjectEnum):
        if not type(name) is SubjectEnum:
            raise ValueError(f'Subject is not allowed: {name}')
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Subject) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Exam:
    TICKET_NUMBER = 5

    def __init__(self, student_group, subject, teacher):
        self.student_group = student_group
        self.subject = subject
        self.teacher = teacher

    def start(self):
        if self.subject not in self.teacher.subjects:
            raise ValueError(f'Teacher does not teach subject: {self.subject}')
        print(f'Starting exam [{self.subject.name}]...')
        for student in self.student_group:
            if self.subject not in student.subjects:
                raise ValueError(f'Student does not study subject: {self.subject}')
            tg = TicketGenerator(self.subject)
            for ticket in tg.generate(self.TICKET_NUMBER):
                student.do_ticket(ticket)
            self.teacher.add_student(student)
        print(f'Finishing exam [{self.subject}]...')

    def __str__(self):
        return 'Exam - ' + self.subject.name


class Ticket:
    _id_counter = 1

    def __init__(self, difficulty, subject, qa_dict):
        self.id = Ticket._id_counter
        Ticket._id_counter += 1
        self.difficulty = difficulty
        self.subject = subject
        self.qa_dict = qa_dict

    def get_questions(self):
        return self.qa_dict

    def add_question(self, question, answer):
        self.qa_dict[question] = answer

    def remove_question(self, question):
        del self.qa_dict[question]

    def __str__(self):
        return f'ID: {self.id}\nDifficulty: {self.difficulty}\nQuestions: {self.qa_dict}'


class TicketGenerator:
    MIN_DIFFICULTY = 1
    MAX_DIFFICULTY = 5

    def __init__(self, subject):
        self.subject = subject

    def generate(self, count):
        for i in range(count):
            difficulty = random.randint(self.MIN_DIFFICULTY, self.MAX_DIFFICULTY)
            fake = Faker()
            qa_dict = {}
            for k in range(difficulty):
                q = f"{fake.sentence().rstrip('.')}?"
                qa_dict[q] = fake.sentence()
            yield Ticket(difficulty, self.subject, qa_dict)


fake = Faker()

s1 = Student(
    fake.first_name(),
    fake.last_name(),
    subjects={Subject(subj) for subj in random.sample(list(SubjectEnum), k=2)}
)

s2 = Student(
    fake.first_name(),
    fake.last_name(),
    subjects={Subject(subj) for subj in random.sample(list(SubjectEnum), k=2)}
)
t = Teacher(
    fake.first_name(),
    fake.last_name(),
    subjects={Subject(subj) for subj in random.sample(list(SubjectEnum), k=2)}
)

sg = StudentGroup('A', (s1, s2))

print(s1, s1.grades)
print(s2, s2.grades)
print(t, t.subjects)

print('\n\n\n')

for i in range(0, 1):
    subj = random.choice(list(t.subjects))
    exam = Exam(sg, subj, t)
    print(exam)
    try:
        exam.start()
    except ValueError as e:
        print(e)
    print(s1, s1.grades)
    print(s2, s2.grades)
    try:
        print(s1, s1.get_avg_grade(subj))
        print(s2, s2.get_avg_grade(subj))
    except ValueError as e:
        print(e)
    print(t, t.students)

# Ошибка
# b = Subject("Biology")
# b.start_lesson(t, (s,))
