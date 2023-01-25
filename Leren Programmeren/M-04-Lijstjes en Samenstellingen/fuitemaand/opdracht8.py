from fruitmand import fruitmand

watermelon = {'name' : 'watermelon',
    'weight' : 1200,
    'color' : 'green',
    'round' : True}
totaal_weight = 0
fruitmand.append(watermelon)
for x in range(len(fruitmand)):
    totaal_weight += fruitmand[x]["weight"]
print(totaal_weight)