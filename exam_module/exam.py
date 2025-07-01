from .ticket_generator import TicketGenerator


class Exam:
    TICKET_NUMBER = 5

    def __init__(self, student_group, subject, teacher):
        self.student_group = student_group
        self.subject = subject
        self.teacher = teacher

    def start(self):
        if self.subject not in self.teacher.subjects:
            raise ValueError(f'Teacher {self.teacher} does not teach subject: {self.subject}')
        print(f'Starting exam [{self.subject.name}]...')
        for student in self.student_group:
            if self.subject not in student.subjects:
                raise ValueError(f'Student {student} does not study subject: {self.subject}')
            tg = TicketGenerator(self.subject)
            for ticket in tg.generate(self.TICKET_NUMBER):
                student.do_ticket(ticket)
            self.teacher.add_student(student)
        print(f'Finishing exam [{self.subject}]...')

    def __str__(self):
        return 'Exam - ' + self.subject.name
