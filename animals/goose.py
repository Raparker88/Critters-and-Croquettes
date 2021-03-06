from datetime import date
from .animal import Animal
from movements import Walking, Swimming

class Goose(Animal, Walking, Swimming):
    """a child of animal parent class"""
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num) 
        Swimming.__init__(self)
        Walking.__init__(self)

    def honk(self): 
        print("The goose honks. A lot")

    def __str__(self):
        return f'{self.name} the Goose'