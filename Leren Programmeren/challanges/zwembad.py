lengte = float(input("Hoeveel meter lang is het zwembad "))
breede =float(input("Hoeveel meter breed is het zwembad "))
hoogte = float(input("Hoeveel meter hoog is het zwembad "))
afstand = float(input("Hoe ver is het in km"))
uitgrave = lengte * breede * hoogte


if uitgrave <= 20:
    vaste_prijs = 100
    if afstand <=50:
        prijs_per_km = 1.25
    else:
        prijs_per_km =  1.15
else:
    vaste_prijs = 250
    if afstand <=50:
        prijs_per_km = 2.15
    else:
        prijs_per_km =  2.05





grond_afvoeren = lengte * breede * hoogte
prijs_grond_afvoeren = grond_afvoeren * 32.5
prijs_uitgrave = uitgrave * 25
prijs_afstand = afstand * prijs_per_km 
totaal = prijs_grond_afvoeren + prijs_uitgrave + vaste_prijs + prijs_afstand
round_total = round(totaal,2)
print(f"Totaal: {totaal} € ")