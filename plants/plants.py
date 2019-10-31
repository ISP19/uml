class Plants:

    def __init__(self, name_type:str, born_year:int, current_year:int):
        self.name_type = name_type
        self.born_year = born_year
        self.current_year = current_year
    

class Rose(Plants):

    def __init__(self, color:str, name_type:str, born_year:int, current_year:int):
        super().__init__(name_type, born_year, current_year)
        self.color = color
        self.age = current_year - born_year
    
    def info(self):
        return "{}-year-old {} {} Rose".format(self.age, self.color, self.name_type)


class Palm(Plants):

    def __init__(self, name_type:str, height:int, born_year:int, current_year:int):
        super().__init__(name_type, born_year, current_year)
        self.height = height
        self.age = current_year - born_year

    def info(self):
        return "{}-year-old {} Palm : {} feet".format(self.age, self.name_type, self.height)
