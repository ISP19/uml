class Teacher:
    """A Teacher Class"""

    def __init__(self, name: str, teacher_id: str, subject: str):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject


class Student:
    """A Student Class"""

    def __init__(self, name: str, std_id: str):
        self.name = name
        self.std_id = std_id


class Classroom:
    """A Classroom Class"""

    def __init__(self, teacher: Teacher):
        self.homeroom_teacher = teacher
        self.student = []

    def add_student(self, student: Student):
        """Add student to classroom"""
        # code omitted

    def remove_student(self, student: Student):
        """Remove student from classroom"""
        # code omitted
