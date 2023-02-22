def vraag_naam_leeftijd():
    naam = input("Wat is je naam? ").lower()
    leeftijd = input("Wat is je leeftijd? ")
    return{"naam":naam, "leeftijd":leeftijd}

personen = []

while True:
    antwoord = vraag_naam_leeftijd()
    MeerNamen = input("Wil  je nog een naam toevogen? ").lower()
    personen.append(antwoord)
    if MeerNamen == "nee":
        break

for persoon in personen:
    print(persoon['naam'], " is ", persoon["leeftijd"], "Jaar")