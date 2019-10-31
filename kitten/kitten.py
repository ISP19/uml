"""
Thanida Jongarnon 6110545538
"""
class Animal:
    """
    Class represents animal
    """
    def __init__(self, name: str, species: str, id_num: str, age: int, alive: bool):
        self.name = name
        self.species = species
        self.id_num = id_num
        self.age = age
        self.alive = True
    def __str__(self):
        """
        Return a document for animal
        """
        return f'ID:{0}, Name:{1}, Species:{2}'.format(self.id_num, self.name, self.species)
    def die(self):
        """
        Animal is able to die
        """
        self.alive = False
class Kitten(Animal):
    """
    Class represent kitten
    """
    def __init__(self, name: str, species: str, id_num: str, age: int):
        """
        Animal superclass Kitten
        """
        super().__init__(name, species, id_num, age)
        self.sell = False
    def sell_kitten(self):
        """
        Sell kitten
        """
        self.sell = True

class Litter():
    """
    Class represent a litter of kittens
    """
    def __init__(self, size: int):
        """
        A group of kitten
        """
        self.size = size
        self.element = []
    def add_kitten(self, kitten: Kitten):
        """
        Add new member of kitten
        """
        self.element.append(kitten)
        self.size += 1
    def del_kitten(self, kitten: Kitten):
        """
        Remove member of kitten
        """
        self.element.remove(kitten)
        self.size -= 1
