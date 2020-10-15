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
hee_haw = Donkey('Hee Haw', 'mountain donkey', 'midday','apples', 908790)
satan = Goat('Satan', 'pygmy goat', 'afternoon','grass', 8654675)
perm = Sheep('Perm', 'curly sheep', 'morning','grass', 837594)
ed = Horse('Mr. Ed', 'Tennessee walking horse', 'midday','oats', 957983)
cuddles = Ratsnake('Cuddles', 'Ratsnake','mice', 87676)
kissy = Copperhead('Kissy', 'Copperhead','mice', 4657)
monty = Python('Monty', 'python','rats', 665679)
cotton = Moccassin('Cotton', 'cotton mouth','frogs', 356554)
rainbow = Coralsnake('Rainbow', 'coral snake','roaches', 108375)
tangerine = Goldfish('Tangerine', 'goldfish','fish flakes', 23987)
waddle = Duck('Waddle', 'mallard','corn kernels', 487589)
ki = Coy('Ki', 'coy','fish flakes', 87984)
ribbit = Frog('Ribbit', 'bull frog','flies', 58769)
the_devil = Goose('The Devil', 'goose','corn kernels', 63495)

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

print(slither_inn.last_critter_added)

miss_fuzz.feed()
tangerine.feed()