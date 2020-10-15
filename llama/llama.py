from datetime import date


class Llama:

    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        self.shift = shift
        self.food = food
        try:
            self.__chip_num = int(chip_num)
        except ValueError:
            print("chip number must be an integer")

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @property
    def chip_num(self):
        try:
            return self.__chip_num
        except AttributeError:
            return 'no chip'
    
    @chip_num.setter
    def chip_num(self, number):
        pass
        
