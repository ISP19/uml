"""
This is classroom
"""
class User:
    """
    User class
    """
    def __init__(self, username: str, password: str, ID: int, course_list: list):
        self.username = username
        self.password = password
        self.ID = ID
        self.course_list = course_list
    def authenticate(self) -> bool:
        """return True or False"""

class Teacher(User):
    """
    Teacher user class
    """
    def __init__(self, user: User):
        super().__init__(user.username, user.password, user.ID, user.course_list)
    def create_course(self, course_name):
        """create course using course_name"""

class Student(User):
    """
    Student user class
    """
    def __init__(self, user: User):
        super().__init__(user.username, user.password, user.ID, user.course_list)
    def choose_course(self, course_name):
        """choose course from teacher"""

class Course:
    """
    Teacher and student course
    """
    def __init__(self, course_name):
        self.name = course_name
