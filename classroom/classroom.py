class Classroom:
    def __init__(self, teacher:Teacher):
        self.homeroom_teacher = teacher
        self.student = []
    
    def add_student(self, student: Student):
        # code omitted
        pass

class Teacher:
    def __init__(self, name:str, id:str, subject: str):
        self.name = name
        self.id = id
        self.subject = subject
    
class Student:
    def __init__(self, name:str, id:str):
        self.name = name
        self.id = id
