import datetime 

class Animal:
    """Class of some animal"""
    def __init__(self , name: str, sex:str,date):
        self.name = name
        self.sex = sex
        self.old = datetime.date - date
        
    
class Zoo:
    """Class of space for keep animal"""
    def __init__(self, name:str):
        self.name = name
        self.all_cage = []

    def add_animal(self,):
        """Medthod for add animal_cage to cage"""
        return 0

class Tiger(Animal):
    def __init__(self, name, sex, date):
        super().__init__(name, sex, date)

    def description(self) -> str:
        print(f"{self.name} sex:{self.sex} date:{self.old}")


class Cage():
    def __init__(self,Animal):
        self.cage = [Animal]

    def add_tiger(self,Animal:Animal):
        self.cage.append(Animal)
        

        




        
        




