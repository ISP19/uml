# 6110545643 sivanat subpaisarn

class Animal():
    def __init__(self, age:int, height:int, weight:int, is_male:bool ):
        self.age=  age
        self.height= height
        self.weight= weight
        self.is_male = is_male

    def eat(self):
        pass


class Wolf(Animal):
    def __init__(self, age, height, weight, breed:string):
        super().__init__(age, height, weight)
        self.breed = breed
        self.pack = None


class WolfPack():
    def __init__(self, size:int):
        self.size = size
        self.member = []
    
    def join_pack(self, Wolf):
        self.member.append(Wolf)
        Wolf.pack =  self
        self.size += 1

    def leave_pack(self, Wolf):
        self.member.remove(Wolf)
        Wolf.pack = None
        self.size -= 1
