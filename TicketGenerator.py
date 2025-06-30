import random
from faker import Faker
from Ticket import Ticket


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
