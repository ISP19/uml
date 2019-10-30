#
# Draw a UML class diagram based on this code.
# Show classes, attributes, and methods and
# relationships between classes such as inheritance,
# association, and dependency.
# Use correct UML notation, show multiplicity where it makes sense.
#
class Animal:
    def __init__(self, name: str, legs: int):
        self.name = name
        self.legs = legs
    
    def change_name(self, name):
        self.name = name
    
    def die(self):
        """Delete this object"""
        # code omitted
        pass


class Turtle(Animal):
    def __init__(self, name: str, legs: int, species: str):
        super().__init__(name, legs)
        self.species = species

    def eat(self, object: object, amount: int):
        """ Decrease seaweed amount or delete seaweed object"""
        # code omitted
        pass


class Seaweed():
    def __init__(self, amount: int):
        self.amount = amount


class Human():
    def __init__(self, name: str):
        self.name = name
        
    def feed(self, animal: Animal):
        """One human can feed food from 0 to many animals"""
        # code omitted
        pass