from fruitmand import fruitmand

watermelon = {'name' : 'watermelon',
    'weight' : 1200,
    'color' : 'green',
    'round' : True}
fruitmand.append(watermelon)
for x in range(len(fruitmand)):
    print(fruitmand[x]["weight"])