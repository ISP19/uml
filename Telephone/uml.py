class Person:
    """
    The class that create the object which is person
    """
    def __init__(self, name, age, telephone):
        self.name = name
        self.age = age
        self.telephone = telephone

    def pick_up(self, person):
        """
        The method print the name of the person that call another person
        """
        print(f"{self.name} pick up {person}")


class Telephone:
    """
    The class that create the object which is Telephone
    """
    def __init__(self, brand, color, price, owner):
        self.brand = brand
        self.color = color
        self.price = price
        self.owner = owner

    def call(self, person):
        """
        The method print the call of the person that call another person
        """
        print(f"{self.owner} calling {person.name}")
        person.pick_up(self.owner)

    def take_a_picture(self, side):
        """
        The method print the side of camera
        """
        print(f"Open {side} camera")


class Student(Person):
    """
        The class that create the object which is Student inherit from person
    """
    def __init__(self, name, age, telephone):
        super().__init__(name, age, telephone)
        self.duty = "Study"
