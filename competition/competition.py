class Person:
    def __init__(self, first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Team(Person):
    def __init__(self,name):
        self.members = []
        self.name = name
    
    def add_member(self,Person):
        self.members.append(Person)

class Competition(Team):
    def __init__(self):
        self.teams = []
    
    def add_group(self,Team):
        self.teams.append(Team)
    
    def delete_group(self,name):
        for team in self.teams:
            if team.name == name:
                self.teams.remove(team)



    

    

