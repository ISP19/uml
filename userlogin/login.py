class Employee:
    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday
class Employer:
    def __init__(self, name, surname,birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday
class Login:
    def __init__(self,id,password):
        self.id = id
        self.password = password
        self.list_id = []

    def add_id(self,user):
        self.list_id.append(user)
    def remove_id(self,user):
        self.list_id.remove(user)




