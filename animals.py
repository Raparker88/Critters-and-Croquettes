# import the python datetime module to help us create a timestamp
from datetime import date
from copperhead import Copperhead
from coralsnake import Coralsnake
from coy import Coy
from donkey import Donkey
from duck import Duck
from frog import Frog
from goat import Goat
from goldfish import Goldfish
from goose import Goose
from horse import Horse
from llama import Llama
from moccassin import Moccassin
from python import Python
from ratsnake import Ratsnake
from sheep import Sheep
from attractions import Wetlands, SnakePit, PettingZoo

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = SnakePit("Slither Inn", "slithering snakes and creepy crawlies")
critter_cove = Wetlands("Critter Cove", "fins and feathers in all colors")

miss_fuzz = Llama('Miss Fuzz', 'domestic llama', 'morning','grass', 12345)
hee_haw = Donkey('Hee Haw', 'mountain donkey', 'midday','apples')
satan = Goat('Satan', 'pygmy goat', 'afternoon','grass')
perm = Sheep('Perm', 'curly sheep', 'morning','grass')
ed = Horse('Mr. Ed', 'Tennessee walking horse', 'midday','oats')
cuddles = Ratsnake('Cuddles', 'Ratsnake','mice')
kissy = Copperhead('Kissy', 'Copperhead','mice')
monty = Python('Monty', 'python','rats')
cotton = Moccassin('Cotton', 'cotton mouth','frogs')
rainbow = Coralsnake('Rainbow', 'coral snake','roaches')
tangerine = Goldfish('Tangerine', 'goldfish','fish flakes')
waddle = Duck('Waddle', 'mallard','corn kernels')
ki = Coy('Ki', 'coy','fish flakes')
ribbit = Frog('Ribbit', 'bull frog','flies')
the_devil = Goose('The Devil', 'goose','corn kernels')

varmint_village.add(miss_fuzz)
varmint_village.add(hee_haw)
varmint_village.add(satan)
varmint_village.add(perm)
varmint_village.add(ed)
slither_inn.add(cuddles)
slither_inn.add(kissy)
slither_inn.add(monty)
slither_inn.add(cotton)
slither_inn.add(rainbow)
critter_cove.add(tangerine)
critter_cove.add(waddle)
critter_cove.add(ki)
critter_cove.add(ribbit)
critter_cove.add(the_devil)

varmint_village.printReport()
slither_inn.printReport()
critter_cove.printReport()

miss_fuzz.chip_num = 6789
print(miss_fuzz.chip_num)
