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
