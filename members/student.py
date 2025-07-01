import random
from .university_member import UniversityMember


class Student(UniversityMember):
    def __init__(self, first_name, last_name=None, age=None, subjects=None, group=None):
        super().__init__(first_name, last_name, age, subjects)
        self.grades = {key: [] for key in self.subjects}
        self.group = group

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f'Student does not study subject: {subject}')
        self.grades[subject].append(grade)

    def leave_group(self):
        self.group = None

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
