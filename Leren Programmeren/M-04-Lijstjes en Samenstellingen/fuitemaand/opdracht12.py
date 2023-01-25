from fruitmand import fruitmand
list = []
max_lengte= 0
for i in range(0,len(fruitmand)):
    lengte_naam= len(fruitmand[i]['name'])
    if lengte_naam > max_lengte:
        max_lengte = lengte_naam
        naam = (fruitmand[i].get('name'))
        kleur = (fruitmand[i].get('color'))
        gewicht = (fruitmand[i].get('weight'))

gewicht_kg = gewicht / 1000

kleuren = {
    "green" : "groene",
    "red" : "rode",
    "orange" : "oranje",
    "brown" : "bruin",
    "black" : "zwart",
    "yellow" : "gele",
    "blue" : "blauw",
    "purple" : "paars",
    "pink" : "roze"
}
print(f'De "{naam}" ({max_lengte} letters) heeft een {kleuren[kleur]} kleur en een gewicht van {gewicht_kg} kg.')