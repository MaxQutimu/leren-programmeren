import random
lijst_met_namen = []
lootjes = []
for_loop = 0
loop = True
loop_voor_lootjes = True

while loop:
    naam = input("Voeg er naam toe ")
    if naam in lijst_met_namen:
        print("Naam bestaat al")
    else:
        lijst_met_namen.append(naam)
        print("Naam wordt toegevoed aan een lijst!")
        if len(lijst_met_namen) > 2:
            meer_namen = input("Wil je nog een naam toegevoegen? ").lower()
            if not meer_namen in ["ja","j","yes","y"]:
                loop = False
lootjes = []
random.shuffle(lijst_met_namen)
len_lijst_met_namen = len(lijst_met_namen)
print("Namen    Lootjes")
for naam in lijst_met_namen:
    next_index = (lijst_met_namen.index(naam) + 1) % len_lijst_met_namen
    lootjes.append(lijst_met_namen[next_index])
    print(f"{naam}    {lootjes}")
ok = True
for i in range(len(lijst_met_namen)):
    if lijst_met_namen[i] == lootjes[i]:
        ok = False





