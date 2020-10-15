# import the python datetime module to help us create a timestamp
from datetime import date


class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        try:
            self.__chip_num = int(chip_num)
        except ValueError:
            print("chip number must be an integer")

        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    @property
    def chip_num(self):
        try:
            return self.__chip_num
        except AttributeError:
            return 'no chip'
    
    @chip_num.setter
    def chip_num(self, number):
        pass


