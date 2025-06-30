from UniversityMember import UniversityMember


class Teacher(UniversityMember):
    def __init__(self, first_name, last_name=None, age=None, subjects=None, students=None):
        super().__init__(first_name, last_name, age, subjects)
        if students is None:
            students = set()
        self.students = students

    def add_student(self, student):
        self.students.add(student)
