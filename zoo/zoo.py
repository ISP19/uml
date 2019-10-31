"""Module of zoo"""

class Animal:
    """Class of some animal"""
    def __init__(self, name: str, sex: str, year: int, type: str):
        self.name = name
        self.sex = sex
        self.old = 2019-year
        self.type = type

    def description(self) -> str:
        """Print description of animal"""
        print(f"{self.type} name:{self.name} sex:{self.sex} date:{self.old} ")

    def get_type(self) -> str:
        """return type of tiger"""
        return self.type

class Zoo:
    """Class of space for keep animal"""
    def __init__(self, name: str):
        self.name = name
        self.all_cage = []

    def add_cage(self, Cage: Cage):
        """Medthod for add animal_cage to cage"""
        self.all_cage.append(Cage)

    def show_cage(self):
        """Show animal in this cage"""
        for cage in self.all_cage:
            print(cage)

class Tiger(Animal):
    """Sub class of Animal"""
    def __init__(self, name: str, sex: str, year: int):
        super().__init__(name, sex, year, 'tiger')

    def raw(self):
        """show the tiger raw"""
        print(f'{self.type} : Chrawwwwww')


class Cage:
    """feild to collect a animal"""
    def __init__(self, Animal: Animal):
        self.cage = [Animal]

    def add_animal(self, Animal: Animal):
        """add new animal to cage"""
        self.cage.append(Animal)

    def show_animal(self):
        """Show animal in this cage"""
        for animal in self.cage:
            animal.description()
