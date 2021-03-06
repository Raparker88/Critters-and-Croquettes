from datetime import date
from .animal import Animal
from movements import Slithering

class Copperhead(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num) 
        Slithering.__init__(self)
    
    def hiss(self): 
        print("The snake hisses. A lot")

    def __str__(self):
        return f'{self.name} the {self.species}'