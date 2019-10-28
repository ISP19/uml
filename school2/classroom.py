class User:
    def __init__(self, username:str, password:str, email:str, ID:int, course_list:list):
        self.username = username
        self.password = password
        self.email = email
        self.ID = ID
        self.course_list = course_list
    def authenticate(self) -> bool:
        """return True or False"""

class Teacher(User):
    def __init__(self, user:User):
        self.user = user
    def create_course(self, course_name):
        """create course using course_name"""

class Student(User):
    def __init__(self, user:User):
        self.user = user
    def choose_course(self, course_name):
        """choose course from teacher"""

class Course:
    def __init__(self):
        self.name = name
    
