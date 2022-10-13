lengte = float(input("Hoeveel meter lang is het zwembad "))
breede =float(input("Hoeveel meter breed is het zwembad "))
hoogte = float(input("Hoeveel meter hoog is het zwembad "))
afstand = float(input("Hoe ver is het in km "))
kleur = input("Afwerking Rood of kleur naar keuze ").lower()
uitgrave = lengte * breede * hoogte
m2 = lengte * breede

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

if uitgrave <= 20:
    prijs_per_m2 = 250
    if kleur == "rood":
        prijs_kleur = m2 * 25
    else:
        prijs_kleur = m2 *100

else:
    prijs_per_m2 = 200
    if kleur == "rood":
        prijs_kleur = m2 * 20
    else:
        prijs_kleur = m2 * 125



grond_afvoeren = lengte * breede * hoogte
prijs_grond_afvoeren = grond_afvoeren * 32.5
prijs_uitgrave = uitgrave * 25
prijs_afstand = afstand * prijs_per_km 
prijs_kleur_totaal = prijs_per_m2 + prijs_kleur
totaal = prijs_grond_afvoeren + prijs_uitgrave + vaste_prijs + prijs_afstand + prijs_kleur
round_uitgrave = round(prijs_uitgrave,2)
round_afvoeren = round(prijs_grond_afvoeren,2)
round_rijkosten = round(prijs_afstand,2)
round_beton_tegels = round(prijs_kleur_totaal,2)
round_totaal = round(totaal,2)

print(f"Offerte voor het zwembad {lengte} x {breede} x {hoogte} totaal m3 = {uitgrave}")
print(f"Uitgraven: {round_uitgrave} € ")
print(f"Afvoeren: {round_afvoeren} € ")
print(f"Voorrijkosten: {round_rijkosten} € ")
print(f"Beton + tegels: {round_beton_tegels} € ")
print("----------------------------------------")
print(f"Totaal: {round_totaal} € ")