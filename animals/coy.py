from datetime import date
from .animal import Animal
from movements import Swimming

class Coy(Animal, Swimming):

    """A child of Animal from animals/animal.py and Swimming
        movements/swimming.py parent classes"""

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num) 
        Swimming.__init__(self)
    
    def gulp(self): 
        print("The fish gulps. A lot")

    def __str__(self):
        return f'{self.name} the {self.species}'