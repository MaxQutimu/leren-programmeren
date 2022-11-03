import random 

naam = input("Wat is je naam? ")
aantal = int(input("Hoeveel complimenten wil je? "))

lijst = ["Je bent geweldig","Je heb mooi haar","You sexy","je heb een mooi schoenen"]
vorige_kans = 0
for x in range(aantal):
    kans = random.choice(lijst)
    while kans == vorige_kans:
        kans = random.choice(lijst)
    if kans != vorige_kans:
        print(f"{kans} {naam}")
    vorige_kans = kans

