"""
This is the zoo, that have 4 objects.

1. Animal
2. Turtle -> A type of animal
3. Seaweed -> Turtle eat seaweed
4. Human -> Feed any food to animals
"""

class Animal:
    "Can be any type of animal, for example, Tiger, Cat, Turtle."
    def __init__(self, name: str, legs: int):
        self.name = name
        self.legs = legs

    def change_name(self, name):
        "Change type of animal"
        self.name = name

    def die(self):
        """Delete this object"""
        # code omitted


class Seaweed():
    "Turtle eat this"
    def __init__(self, amount: int):
        self.amount = amount

    def decrease(self, amount: int):
        "Decrease amount of Seaweed"
        self.amount -= amount


class Turtle(Animal):
    "A type of animal, but adding species to the field."
    def __init__(self, name: str, legs: int, species: str):
        super().__init__(name, legs)
        self.species = species

    def eat(self, food: Seaweed, amount: int):
        """ Decrease seaweed amount or delete seaweed object"""
        # code omitted


class Human():
    "Task of human is to feed the animal"
    def __init__(self, name: str):
        self.name = name

    def feed(self, animal: Animal):
        """One human can feed food from 0 to many animals"""
        # code omitted
