class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    def printReport(self):
        print(f'{self.attraction_name} is where you\'ll find {self.description} of all sizes including')
        for animal in self.animals:
            print(f'* {animal.name} the {animal.species}')