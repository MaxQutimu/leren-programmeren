opgeslagen = {"bolletjes": 0 ,
              "aardbei": 0,
              "chocolade": 0,
              "munt": 0,
              "vanille" :0,
              "prijs_per_bol": 1.10,
              "slagroom": 0,
              "slagroom_prijs" : 0.50,
              "sprinkels": 0,
              "sprinkels_prijs": 0.30,
              "carmel"  :0,
              "carmel_prijs" :[0.60, 0.90],
            "hoorntje_bakje":{"bakje":0,
                            "prijs_per_bakje": 0.75,
                           "hoorntje":0,
                           "prijs_per_hoorntje":1.25}}  
bestellingen = []
def vraag_bolletjes():
    while True:
        try:
            bolletjes = int(input("aantal bolletjes "))
            if bolletjes <= 0:
                print('Vul getal groter dan 0')
            elif bolletjes <= 8:
                break 
            elif bolletjes >= 8:
                print('Sorry, zulke grotebakken hebben we niet')
            else:
                print('Sorry ik snap het niet')
        except:
            print("vul een cijfer in")
    return bolletjes


def vraag_bakje(bolletjes):
    hoorntje_of_bakje = 'bakje'
    if bolletjes <= 3:
            while True:
                try:
                    hoorntje_of_bakje = str(input(f'Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje? '))
                    if hoorntje_of_bakje == 'hoorntje' or 'baakje' :
                        break
                    else:
                        print('sorry ik snap het niet')
                except:
                    print("Je kan allen kiezen tussen hoorntje of bakje")
    print(f"hier is uw {hoorntje_of_bakje} met {bolletjes} bolletje(s)")
    return hoorntje_of_bakje

def opslag(bolletjes , hoorntje_of_bakje):
    opgeslagen["bolletjes"] += bolletjes
    opgeslagen["hoorntje_bakje"][hoorntje_of_bakje] += 1
    return True

def bestelling(bolletjes, hoorntje_of_bakje):
    bestellingen.append(f"\n{bolletjes} x bolletjes in het {hoorntje_of_bakje}")
    return True

def smaken(bolletjes):
    while True:
        for bol in range(bolletjes):
            bol_teller = bol +1
            smaak = input(f"Welke smaak wilt u voor een bolletje nummer {bol_teller} \n A)Aardbei \n C)Chocolade \n M)Munt \n V)Vanille").lower()
            if bol == bolletjes:
                break
            elif smaak == 'a':
                opgeslagen["aardbei"] += 1
            elif smaak == 'c':
                opgeslagen["chocolade"] += 1
            elif smaak == 'm':
                opgeslagen["munt"] += 1
            elif smaak == 'v':
                opgeslagen["vanille"] +=1
            else:
                print('Kies een juiste smaak')
        return True
def toppings():
    while True:
        try:
            toppings_or_not = input("Wilt u toppings er bij?").lower()
            if toppings_or_not in ['ja','yes','y']:
                while True:
                    try:
                        topping = input("Wat voor toppings wilt u? \n A)Slaagroom \n B)Sprinkels \n C) Caramel Saus ").lower()
                        if topping == 'a':
                            opgeslagen['slagroom'] += 1
                            break
                        if topping == 'b':
                            opgeslagen['sprinkels'] += 1
                            break
                        if topping == 'c':
                            opgeslagen["carmel"] +1
                            break
                        else:
                            print("kies juiste topping")
                    except:
                        print('sorry ik snap het niet')
            else:
                break
        except:
            print('sorry ik snap het niet')
def meer_bestellen():
    while True:
        meer = input('Wilt u meer bestelen? ')
        if meer in ["ja","nee"]:
            break
        else:
            print('Ik snap het niet')
    return meer

def totaale_kosten():
    # totaal_bolletjes = opgeslagen["bolletjes"] * opgeslagen["prijs_per_bol"]
    # print(f"Bolletje(s)     {opgeslagen['bolletjes']} x {format(opgeslagen['prijs_per_bol'],'.2f')} = {format(totaal_bolletjes,'.2f')}")
    # totaal = totaal_bolletjes
    totaal = 0
    totaal_toppings = 0
    if opgeslagen["aardbei"] != 0:
        totaal_bolletjes_aardbei = opgeslagen["aardbei"] * opgeslagen["prijs_per_bol"]
        print(f"B.aardbei      {opgeslagen['aardbei']} x {format(opgeslagen['prijs_per_bol'],'.2f')} = {format(totaal_bolletjes_aardbei,'.2f')}")
        totaal += totaal_bolletjes_aardbei
    if opgeslagen["chocolade"] != 0:
        totaal_bolletjes_chocolade = opgeslagen["chocolade"] * opgeslagen["prijs_per_bol"]
        print(f"B.chocolade    {opgeslagen['chocolade']} x {format(opgeslagen['prijs_per_bol'],'.2f')} = {format(totaal_bolletjes_chocolade,'.2f')}")
        totaal += totaal_bolletjes_chocolade
    if opgeslagen["munt"] != 0:
        totaal_bolletjes_Munt = opgeslagen["munt"] * opgeslagen["prijs_per_bol"]
        print(f"B.munt     {opgeslagen['munt']} x {format(opgeslagen['prijs_per_bol'],'.2f')} = {format(totaal_bolletjes_Munt,'.2f')}")
        totaal += totaal_bolletjes_Munt
    if opgeslagen["vanille"] != 0:
        totaal_bolletjes_vanille = opgeslagen["vanille"] * opgeslagen["prijs_per_bol"]
        print(f"B.vanille     {opgeslagen['vanille']} x {format(opgeslagen['prijs_per_bol'],'.2f')} = {format(totaal_bolletjes_vanille,'.2f')}")
        totaal += totaal_bolletjes_vanille
    if opgeslagen["hoorntje_bakje"]["bakje"] != 0:
        totaal_bakje = opgeslagen["hoorntje_bakje"]["bakje"] * opgeslagen["hoorntje_bakje"]["prijs_per_bakje"]
        print(f"Bakje(s)    {opgeslagen['hoorntje_bakje']['bakje']} x {format(opgeslagen['hoorntje_bakje']['prijs_per_bakje'],'.2f')} = {format(totaal_bakje,'.2f')}")
        totaal += totaal_bakje
    if opgeslagen["hoorntje_bakje"]["hoorntje"] != 0:
        totaal_hoorntje = opgeslagen["hoorntje_bakje"]["hoorntje"] * opgeslagen["hoorntje_bakje"]["prijs_per_hoorntje"]
        print(f"Hoorntje(s)    {opgeslagen['hoorntje_bakje']['hoorntje']} x {format(opgeslagen['hoorntje_bakje']['prijs_per_hoorntje'],'.2f')} = {format(totaal_hoorntje,'.2f')}")
        totaal += totaal_hoorntje
    if opgeslagen["slagroom"] != 0:
        totaal_toppings += opgeslagen["slagroom"] * opgeslagen["slagroom_prijs"]
        totaal += totaal_toppings
    if opgeslagen["sprinkels"] != 0:
        totaal_toppings += opgeslagen["sprinkels"] * opgeslagen["sprinkels_prijs"]
        totaal += totaal_toppings
    if opgeslagen["carmel"] !=0:
        if opgeslagen["hoorntje_bakje"]["bakje"] != 0:
            totaal_toppings += opgeslagen["carmel"] * opgeslagen["carmel_prijs"][1]
            totaal += totaal_toppings
        else:
            totaal_toppings += opgeslagen["carmel"] * opgeslagen["carmel_prijs"][0]
            totaal += totaal_toppings

    print(f"Topping(s) =              {format(totaal_toppings,'.2f')}" )
    print(f"\ntotaal =                 {format(totaal,'.2f')}")
    return True

def ijssalon(bolletjes,hoorntje_of_bakje):
    while True:
        bolletjes = vraag_bolletjes()
        hoorntje_of_bakje = vraag_bakje(bolletjes)
        smaken(bolletjes)
        toppings()
        opslag(bolletjes, hoorntje_of_bakje)
        bestelling(bolletjes, hoorntje_of_bakje)
        verder = meer_bestellen()
        if verder == "nee":
            break
    return True

def bon(hoorntje_of_bakje):
    print("-----------Bon----------")
    print(*bestellingen)
    totaale_kosten()
    bestellingen.clear()










