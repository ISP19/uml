# 6110545554 Tetach Rattanavikran

class Diplodocus():
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
        self.eating = None

class Rock():
    def __init__(self, size):
        self.size = size


class Gastrolith():
    def __init__(self):
        self.rock = []
        self.number = 0

    def eating(self):
        """ Diplodocus will eat rock(gastrolith) with their food to help with digestion. """
        self.rock.append(Rock)
        Diplodocus.eating = self
        self.number += 1

    def defecate(self):
        self.rock.remove(Rock)
        Diplodocus.eating = None
        self.number -= 1
