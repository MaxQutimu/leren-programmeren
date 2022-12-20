from fruitmand import fruitmand
list = []
max_lengte= 0
for index in range(0,len(fruitmand)):
    lengte_naam= len(fruitmand[index]['name'])
    if lengte_naam > max_lengte:
        max_lengte = lengte_naam
        naam = (fruitmand[index].get('name'))
        kleur = (fruitmand[index].get('color'))
        gewicht = (fruitmand[index].get('weight'))



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
print(f'De "{naam}" ({max_lengte} letters) heeft een {kleuren[kleur]} kleur en een gewicht van {gewicht / 1000} kg.')