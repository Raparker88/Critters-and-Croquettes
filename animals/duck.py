from datetime import date
from .animal import Animal
from movements import Walking, Swimming

class Duck(Animal, Walking, Swimming):

    """a child of animal, walking and swimming parent class. Unique method self.quack()"""

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num) 
        Swimming.__init__(self)
        Walking.__init__(self)

    def quack(self): 
        print("The goose honks. A lot")

    def __str__(self):
        return f'{self.name} the {self.species}'