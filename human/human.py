#6010545960 Ingkharat Jangchud
class Human:
    def __init__(self, sex, age, height, weight,name):
        self.sex = sex
        self.age = age
        self.heigh = height
        self.weight = weight
        self.name = name
    

class SpiderMan(Human):

    def __init__(self, sex,age,height,weight):
        self.sex = sex
        self.age = age
        self.heigh= height
        self.weight = weight
        super().__init__(self.sex,self.age,self.heigh,self.weight,'Peter Parker')
    

class Prayut(Human):

    def __init__(self, sex,age,height,weight):
        self.sex = sex
        self.age = age
        self.heigh= height
        self.weight = weight
        super().__init__(self.sex,self.age,self.heigh,self.weight,'Prayut Junochar')
        