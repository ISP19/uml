class Pets:
    def __init__(self, owner):
        self.owner = owner

class Dog(Pets):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
        return "self.name, self.age, self.breed" #string

    def check_owner(self):
        return self.owner

class Puppy(Pets):
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother
    
    def check_parent(self, parent: Dog):
        # code omitted
        return True #boolean

