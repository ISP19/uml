# Draw a UML class diagram based on this code.
# Show classes, attributes, and methods and
# relationships between classes such as inheritance,
# association, and dependency.
# Use correct UML notation, show multiplicity where it makes sense.


class Dog:
    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self, sound: str) -> str:
        return f'{self.name} is barking {sound*int(2)}!'


class Labrador(Dog):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        super().__init__(self.name, 'Labrador', self.age)

    def retrive(self, object: str) -> str:
        return f'{self.name} is retrieving {object}'


class Chihuahua(Dog):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        super().__init__(self.name, 'Chihuahua', self.age)
