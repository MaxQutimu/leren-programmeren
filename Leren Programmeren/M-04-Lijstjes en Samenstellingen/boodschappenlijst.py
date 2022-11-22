BoodSchappenLijst = {}
MeerProducten = True

while MeerProducten:
    Product = input("Wat wil je toevegen?: ").lower()
    while True:
        try:
            aantal = int( input("Hoeveel keer wil je het toevegen?: ") )
            break
        except:
            print("Voer geldig nummer in!")

    if Product in BoodSchappenLijst.keys():
        BoodSchappenLijst[Product] += aantal
    else:
        BoodSchappenLijst.update({Product : aantal})

    while True:
        Toevoegen = input("Wil je nog iets aan je lijst toevoegen?: ").lower()
        if Toevoegen in ["j", "ja","y","yes","ye"]:
            break
        elif Toevoegen in ["n", "nee","no"]:
            MeerProducten = False
            break
        else:
            print("onjuiste antwoord [Y/N]")

print(f"Dat zijn je boodschappen {BoodSchappenLijst}")