opgeslagen = {"bolletjes": 0 ,
              "liters": 0 ,
              "prijs_per_bol": 1.10,
              "prijs_per_liter":9.80,
              "smaken":{
                 "aardbei": 0,
                 "chocolade": 0,
                 "munt": 0,
                 "vanille" :0},
              "toppings":{
                "slagroom": 0,
                "slagroom_prijs" : 0.50,
                "sprinkels": 0,
                "sprinkels_prijs": 0.30,
                "carmel"  :{
                    "carmel_bakje": 0,
                    "carmel_hoorntje": 0,
                    "carmel_prijs":[0.60,0.90]}},
              "hoorntje_bakje":{"bakje":0,
                            "prijs_per_bakje": 0.75,
                           "hoorntje":0,
                           "prijs_per_hoorntje":1.25}}  
bestellingen = []

def vraag_soort_klant():
    while True:
        zakelijke_of_particuliere_klant = input("Z)Zakkelijk of P)Partuculiere klant? ").lower()
        if zakelijke_of_particuliere_klant == "z":
            soort_klant = "zakkelijk"
            return soort_klant

        elif zakelijke_of_particuliere_klant == "p":
            soort_klant = "particuliere"
            return soort_klant
        else:
            print("Onjuiste keuze")

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

def vraag_liters_ijs():
    while True:
        LitersIjs = int(input("Hoeveel liters van ijs wilt uw?"))
        if LitersIjs <= 0:
            print("vul getal die grooter is dan 0")
        else:
            return LitersIjs

def aantal_bolletjes_of_liters(soort_klant):
    if soort_klant == "zakkelijk":
        eenheid = vraag_liters_ijs()
        return eenheid
    else:
        eenheid = vraag_bolletjes()
        return eenheid


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
    # print(f"hier is uw {hoorntje_of_bakje} met {bolletjes} bolletje(s)")
    return hoorntje_of_bakje


        

def opslag(soort_klant,eenheid, hoorntje_of_bakje):
    if soort_klant == "particuliere":
        opgeslagen["bolletjes"] += eenheid
        opgeslagen["hoorntje_bakje"][hoorntje_of_bakje] += 1
    else:
        print(eenheid)
        opgeslagen["liters"] += eenheid
        opgeslagen["hoorntje_bakje"][hoorntje_of_bakje] = 0
    return True


def smaken(eenheid,soort_klant):
    while True:

        for bol in range(eenheid):
            bol_teller = bol +1
            if soort_klant == 'particuliere':
                print(f"Welke smaak wilt u voor een bolletje nummer {bol_teller}")
            else:
                print(f"Welke smaak wilt u voor een liter nummer {bol_teller}")
            smaak = input(f" \n A)Aardbei \n C)Chocolade \n M)Munt \n V)Vanille").lower()
            if bol == eenheid:
                break
            elif smaak == 'a':
                opgeslagen["smaken"]["aardbei"] += 1
            elif smaak == 'c':
                opgeslagen["smaken"]["chocolade"] += 1
            elif smaak == 'm':
                opgeslagen["smaken"]["munt"] += 1
            elif smaak == 'v':
                opgeslagen["smaken"]["vanille"] +=1
            else:
                print('Kies een juiste smaak')
                bol_teller -= 1
        return True
    
def toppings(hoorntje_of_bakje):
    while True:
        toppings_or_not = input("Wilt u toppings er bij?").lower()
        if toppings_or_not in ['ja','yes','y','nee','no','n']:
            break
    if toppings_or_not in ['ja','yes','y']:
        while True:
                topping = input("Wat voor toppings wilt u? \n A)Slaagroom \n B)Sprinkels \n C) Caramel Saus ").lower()
                if topping in ('a','b','c'):
                    break
                else:
                    print("kies juiste topping")
        if topping == 'a':
            opgeslagen["toppings"]['slagroom'] += 1
        if topping == 'b':
            opgeslagen["toppings"]['sprinkels'] += 1
        if topping == 'c':
            if hoorntje_of_bakje == 'hoorntje':
                opgeslagen["toppings"]["carmel"]["carmel_hoorntje"] += 1
            else:
                opgeslagen["toppings"]["carmel"]["carmel_bakje"] += 1
            
            

                        
                    
            
        
def meer_bestellen():
    while True:
        meer = input('Wilt u meer bestelen? ')
        if meer in ["ja","nee"]:
            break
        else:
            print('Ik snap het niet')
    return meer

def totaale_kosten(soort_klant):
    # totaal_bolletjes = opgeslagen["bolletjes"] * opgeslagen["prijs_per_bol"]
    # print(f"Bolletje(s)     {opgeslagen['bolletjes']} x {format(opgeslagen['prijs_per_bol'],'.2f')} = {format(totaal_bolletjes,'.2f')}")
    # totaal = totaal_bolletjes
    totaal = 0
    totaal_toppings = 0
    for smaak in opgeslagen['smaken']:
        if opgeslagen['smaken'][smaak] !=0:
            if soort_klant == 'particuliere':
                totaal_bolletjes_smaak = opgeslagen["smaken"][smaak] * opgeslagen["prijs_per_bol"]
                print(f"B.{smaak}      {opgeslagen['smaken'][smaak]} x {format(opgeslagen['prijs_per_bol'],'.2f')} = {format(totaal_bolletjes_smaak,'.2f')}")
                totaal += totaal_bolletjes_smaak
            elif soort_klant == "zakkelijk":
                totaal_bolletjes_smaak = opgeslagen["smaken"][smaak] * opgeslagen["prijs_per_liter"]
                print(f"L.{smaak}      {opgeslagen['smaken'][smaak]} x {format(opgeslagen['prijs_per_liter'],'.2f')} = {format(totaal_bolletjes_smaak,'.2f')}")
                totaal += totaal_bolletjes_smaak

    if opgeslagen["hoorntje_bakje"]["bakje"] != 0:
        totaal_bakje = opgeslagen["hoorntje_bakje"]["bakje"] * opgeslagen["hoorntje_bakje"]["prijs_per_bakje"]
        print(f"Bakje(s)       {opgeslagen['hoorntje_bakje']['bakje']} x {format(opgeslagen['hoorntje_bakje']['prijs_per_bakje'],'.2f')} = {format(totaal_bakje,'.2f')}")
        totaal += totaal_bakje
    if opgeslagen["hoorntje_bakje"]["hoorntje"] != 0:
        totaal_hoorntje = opgeslagen["hoorntje_bakje"]["hoorntje"] * opgeslagen["hoorntje_bakje"]["prijs_per_hoorntje"]
        print(f"Hoorntje(s)    {opgeslagen['hoorntje_bakje']['hoorntje']} x {format(opgeslagen['hoorntje_bakje']['prijs_per_hoorntje'],'.2f')} = {format(totaal_hoorntje,'.2f')}")
        totaal += totaal_hoorntje
    if opgeslagen["toppings"]["slagroom"] != 0:
        totaal_toppings += opgeslagen["toppings"]["slagroom"] * opgeslagen["toppings"]["slagroom_prijs"]
        totaal += totaal_toppings
    if opgeslagen["toppings"]["sprinkels"] != 0:
        totaal_toppings += opgeslagen["toppings"]["sprinkels"] * opgeslagen["toppings"]["sprinkels_prijs"]
        totaal += totaal_toppings
    if opgeslagen["toppings"]["carmel"]["carmel_bakje"] !=0:
        totaal_toppings += opgeslagen["toppings"]["carmel"]["carmel_prijs"][1]
        totaal += totaal_toppings
    if opgeslagen["toppings"]["carmel"]["carmel_hoorntje"] !=0:
        totaal_toppings += opgeslagen["toppings"]["carmel"]["carmel_prijs"][0]
        totaal += totaal_toppings
    if soort_klant == "particuliere":
        print(f"Topping(s) =              {format(totaal_toppings,'.2f')}" )
    print(f"\ntotaal =                 {format(totaal,'.2f')}")
    if soort_klant == "zakkelijk":
        btw = totaal / 100 * 9
        print(f"BTW 9% {format(btw,'.2f')}")
    return True





def ijssalon(hoorntje_of_bakje):
    soort_klant = False
    while True:
        if soort_klant == False:
            soort_klant = vraag_soort_klant()
        aantal = aantal_bolletjes_of_liters(soort_klant)
        if soort_klant == "particuliere":
            vraag_bakje(aantal)
            smaken(aantal,soort_klant)
            topping = toppings(hoorntje_of_bakje)
            opslag(hoorntje_of_bakje,aantal,topping) 
            verder = meer_bestellen()
            if verder == "nee":
                break
        else:
            smaken(aantal,soort_klant)
            opslag(soort_klant,aantal,hoorntje_of_bakje)
            break
    totaale_kosten(soort_klant)
    
        
        
    return True











