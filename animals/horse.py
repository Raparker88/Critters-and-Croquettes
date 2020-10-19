from datetime import date
from .animal import Animal
from movements import Walking

class Horse(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift 
    
    def nay(self): 
        print("The horse nays. A lot")

    def __str__(self):
        return f'{self.name} the {self.species}'