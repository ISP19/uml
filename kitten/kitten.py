class Animal:
    """Class represents data of animals"""
    def __init__(self, name:str, species:str, id:str, age:int):
        self.name = name
        self.species = species
        self.id = id
        self.age = age
    
    def alive(self):
        pass

    def reproduce(self):
        pass

class Kitten(Animal):
    def __init__(self, name:str, species:str, id:str, age:int):
        super().__init__(name, species, id, age)
    
    def __str__(self):
        pass

class Litter():
    """Class represent a litter of kittens"""
    def __init__(self):
        self.member = []
    
    def add_kitten(self, Kitten):
        pass
    
    def del_kitten(self, Kitten):
        pass

# Thanida Jongarnon 6110545538
    