class Goat:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        self.shift = shift