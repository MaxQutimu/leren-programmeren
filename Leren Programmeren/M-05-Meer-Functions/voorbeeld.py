def vraag_leeftijd_gebruiker(vraag: str) -> int:
    while True:
        leeftijd_string = input(vraag)
        if not leeftijd_string.isnumeric():
            print("voer een getal in")
        elif int(leeftijd_string) > 130:
            print("Zo oud is nog niemand geworden!")
        elif int(leeftijd_string) < 0:
            print("U moet nog geboren worden")
        else:
            leeftijd = int(leeftijd_string)
            break
    return leeftijd
def is_achttien(age : int) -> bool:
    voldoet = False
    if age >= 18:
        voldoet = True
        return voldoet
    

naam = input("Hoe heet je?")
leeftijd = vraag_leeftijd_gebruiker("Hoe oud ben je?")
jaren = is_achttien()
if voldoet == True:
    print
print(f"hoi {naam}, je bent {leeftijd} oud en {jaren}")