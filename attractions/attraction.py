class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

    def printReport(self):
        print(f'{self.attraction_name} is where you\'ll find {self.description} of all sizes including')
        for animal in self.animals:
            print(f'* {animal.name} the {animal.species}')

    @property
    def last_critter_added(self):
        lastCritter = self.animals[-1]
        return (f'{lastCritter.name} the {lastCritter.species}')

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)