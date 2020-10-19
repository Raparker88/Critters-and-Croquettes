from datetime import date
from .animal import Animal
from movements import Swimming, Walking

class Frog(Animal, Swimming, Walking):

    """a child of animal, walking and swimming parent classes"""

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num) 
        Swimming.__init__(self)
        Walking.__init__(self)

    def croak(self): 
        print("The frog croaks. A lot")

    def __str__(self):
        return f'{self.name} the {self.species}'