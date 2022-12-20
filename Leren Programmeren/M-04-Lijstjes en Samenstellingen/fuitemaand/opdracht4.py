from fruitmand import fruitmand
import random
AANTAL = int(input("vul cijfer er in "))


for x in range(AANTAL):
    RandomFruit = random.choice(fruitmand)
    print(RandomFruit['name'])