from datetime import date
from animals import Animal

class Goldfish:

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num) 
        self.swimming = True