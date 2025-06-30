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
