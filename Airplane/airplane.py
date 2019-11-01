class Passengers:
    #Contains info on individuals passengers such as names and age"
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}"

class Captain:
    #Contains info on indivduals captains such as names and age"
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}"

class Airplane:
    #Contains name, models, capacity, captain(s), and list of passengers)
    def __init__(self, name: str, model: str, capacity: int = 0
                ,captain: Captain = ""):
        self.name = name
        self.model = model
        self.capacity = capacity
        self.captain = captain
        self.passengers = []
        
    def __str__(self):
        return f"{self.name}"

    def add_passengers(self, passenger: Passengers):
        self.passengers.append(passenger)

    def add_captain(self, captain: Captain):
        self.captain = captain