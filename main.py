import random
from faker import Faker
from SubjectEnum import SubjectEnum
from Student import Student
from StudentGroup import StudentGroup
from Teacher import Teacher
from Subject import Subject
from Exam import Exam

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
