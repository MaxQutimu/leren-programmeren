from fruitmand import fruitmand
for x in range(len(fruitmand)):
    if fruitmand[x]['name'] == 'druif':
         del fruitmand[x]
         break
for i in range(len(fruitmand)):
    print(fruitmand[i]['color'])
    
     



     