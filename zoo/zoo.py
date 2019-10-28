import datetime 

class Animal:
    """Class of some animal"""
    def __init__(self , name: str, sex:str, year: int):
        self.name = name
        self.sex = sex
        self.old = 2019-year
        
    
class Zoo:
    """Class of space for keep animal"""
    def __init__(self, name:str):
        self.name = name
        self.all_cage = []

    def add_animal(self,Cage: Cage):
        """Medthod for add animal_cage to cage"""
        self.all_cage.append(Cage)

class Tiger(Animal):
    def __init__(self, name: str, sex : str, year:int):
        super().__init__(name, sex, year)

    def description(self) -> str:
        print(f"Tiger name:{self.name} sex:{self.sex} date:{self.old} ")


class Cage:
    def __init__(self,Animal : Animal):
        self.cage = [Animal]

    def add_tiger(self,Animal:Animal):
        self.cage.append(Animal)
        

        




        
        




