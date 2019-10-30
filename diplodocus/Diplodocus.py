# 6110545554 Tetach Rattanavikran


class Diplodocus():
    """ General composition of Diplodocus. """
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
        self.eating = None


class Rock():
    """ Stomach stone or gizzard stone which is ingested and pass through the digestive system. """
    def __init__(self, size):
        self.size = size


class Gastrolith():
    """ It will eat rocks(Gastrolith) with their food to help with digestion. """
    def __init__(self):
        self.rock = []
        self.number = 0

    def eating(self):
        """ When it eats, a number of rocks(Gastrolith) will be increased. """
        self.rock.append(Rock)
        Diplodocus.eating = self
        self.number += 1

    def defecating(self):
        """ When it defecates, a number of rocks(Gastrolith) will be decreased. """
        self.rock.remove(Rock)
        Diplodocus.eating = None
        self.number -= 1
