from exam_module import Subject


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
