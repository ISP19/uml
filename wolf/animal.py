
"""
# 6110545643 sivanat subpaisarn UML assignment. 30 Oct 2019
"""

class Animal():
    """
    Base class for all animal
    """
    def __init__(self, age: int, height: int, weight: int, is_male: bool):
        """
        base class for Animal
        """
        self.age = age
        self.height = height
        self.weight = weight
        self.is_male = is_male
        self.alive = True

    def eat(self):
        """
        animal have basic function eat
        """
        self.weight += 1

    def die(self):
        """
        animal have basic property alive
        """
        self.alive = False


class Wolf(Animal):
    """
    Class Wolf - Animal Superclass.
    """
    def __init__(self, age, height, weight, breed: str):
        """
        Animal superclass Wolf
        """
        super().__init__(age, height, weight)
        self.breed = breed
        self.pack = None
        self.smell = None

    def sniff(self, surroundings: list):
        """
        wolf has almost 200 million scent cells and
        can smell animals from more than 1 mi (1.6 km) away.
        """
        self.smell = surroundings[0]


class WolfPack():
    """
    Class WolfPack - Wolf class container.
    """
    def __init__(self, size: int):
        """
        WolfPack is pack of class Wolf
        """
        self.size = size
        self.member = []

    def join_pack(self, wolf: Wolf):
        """
        Wolf can join WolfPack
        """
        self.member.append(wolf)
        wolf.pack = self
        self.size += 1

    def leave_pack(self, wolf: Wolf):
        """
        Wolf can leave WolfPack
        """
        self.member.remove(wolf)
        wolf.pack = None
        self.size -= 1
