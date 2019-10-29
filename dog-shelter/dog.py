# Draw a UML class diagram based on this code.
# Show classes, attributes, and methods and
# relationships between classes such as inheritance,
# association, and dependency.
# Use correct UML notation, show multiplicity where it makes sense.


class Dog:
    """A class represent Dog"""

    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self, sound: str) -> str:
        return f'{self.name} is barking {sound*int(2)}!'


class Shelter:
    """A class represent shelter """

    def __init__(self, dog_list: list = []):
        """Shelter constucter"""
        self.dog_list = dog_list

    def add_dog(self, dog: Dog):
        """Class method to add Dog into shelter"""
        self.dog_list.append(dog)

    def euthanize(self, lucky_dog_name: str, lucky_dog_breed: str, lucky_dog_age: int):
        """Class method to get rid of unwanted dog"""
        for dog in self.dog_list:
            if dog.name == lucky_dog_name and dog.breed == lucky_dog_breed and dog.age == lucky_dog_age:
                self.dog_list.remove(dog)
        return f'{dog.name} has been killed'


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
