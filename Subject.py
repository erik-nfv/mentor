from SubjectEnum import SubjectEnum


class Subject:
    MIN_GRADE = 1
    MAX_GRADE = 5

    def __init__(self, name):
        if not type(name) is SubjectEnum:
            raise ValueError(f'Subject is not allowed: {name}')
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Subject) and self.name == other.name

    def __hash__(self):
        return hash(self.name)
