import random
from random import randint
score = 0
rondes = int(input("Hoeveel rondes wil je spelen "))
while rondes >=21 :
    rondes = int(input("Hoeveel rondes wil je spelen(max 20) "))
rondeteller = 1
spel = True
while spel:
    doorspelen = True
    raad = 0
    
    while doorspelen:
        cijfer = randint(1,1000)
        maxraad = 0
        print(f"round {rondeteller}")
        print(f"Jouw score {score}")
        while doorspelen:
            raad = int(input("Raad je cijfer "))
            verschil = cijfer - raad
            abs(verschil)
            print(cijfer)
            if maxraad >= 10:
                print("Je hebt al 10 keer geraden")
                doorspelen = False
                rondes = rondes - 1
                rondeteller = rondeteller + 1
                if rondes <= 0:
                    spel = False
                else:
                    end=input("Wil je volgende ronde gaan spelen? ")
                    if end in ["no","n","nee"]:
                        spel = False
            
            else:
                if raad == cijfer:
                    score = score + 1
                    print("Je Heb het goed geraden! ")
                    print(f"Juiste cijfer was {cijfer} ")
                    rondes = rondes - 1
                    doorspelen = False
                    rondeteller = rondeteller + 1
                    if rondes <= 0:
                        spel = False
                    else:
                        end=input("Wil je volgende ronde gaan spelen? ")
                        if end in ["no","n","nee"]:
                            spel = False
                elif cijfer >= raad:
                    if verschil <= 50:
                        print("Warm, hoger")
                    else:
                        print("Hoger")
                    maxraad = maxraad + 1
                elif cijfer <= raad:
                    if verschil <= 50:
                        print("Warm, lager")
                    else:
                        print("Lager")
                    maxraad = maxraad + 1
                
print(f"Jouw eind score is {score}")
print(f"Rounds gespeeld {rondeteller}")

            




