score = 0
ervaring = input('''heeft uw ervaring in een van deze vakken?
1. Dieren Dressuur
2. Jongleren
3. Acrobatiek
''')
if ervaring == "Dieren dressur":
    Dieren_dressuur = int(input('Hoeveel jaar prijktijkervaring heeft uw met dieren-dressuur?'))
    if Dieren_dressuur > 4:
        score = score + 1
    else:
     score = score + 0
     
    
elif ervaring =="Jongleren":
    Jongleren = int(input('Hoeveel jaar ervaring heeft uw met Jongleren?'))
    if Jongleren > 5:
        score = score + 1
    else:
     score = score + 0

else:
    ervaring == "Acrobatiek"
    Acrobatiek = int(input('Hoeveel jaar prijktijkervaring heeft uw met acrobatiek?'))
    if Acrobatiek > 3:
        score = score + 1
    else:
     score = score + 0


Diploma = input('Heeft uw MBO-4 of hooger behaald?')

if Diploma in ("Ja","ja","j"):
    score = score + 1
else:
    score = score + 0


Rijbewijs = input('Heeft uw een Vrachtwagen rijbewijs?')
if Rijbewijs in ("Ja","ja","j"):
    score = score + 1
    
else: 
    score = score + 0
    
geslacht = input('bent uw man of vrouw?')
if geslacht in ("Man","man"):
    snor = int(input('Hoe groot is uw snor?'))
    if snor > 10:
        score = score + 1
    elif snor == 10:
        score = score + 1
    
    else: 
        score = score + 0



else: 
    geslacht in ("vrouw","Vrouw")
    krulhaar = int(input('Hoelang is uw haar?'))
    if krulhaar > 20:
        score = score + 1
    elif krulhaar == 20:
        score = score + 1
    else: 
        score = score + 0

lang = int(input('Hoe lang bent uw?'))
if lang > 150:
    score = score + 1

elif lang == 150:
    score = score + 1

else:
    score = score + 0
    

zwaar = int(input('Hoe zwaar bent uw?'))
if zwaar < 90:
    score = score + 1
elif zwaar == 90:
    score = score + 1
else:
    zwaar > 90
    score = score + 0
certificat = input('Heeft Certificaat uw Overleven met gevaarlijk personeel?')
if certificat in ("ja","Ja","J"):
    score = score + 1
else:
    score = score + 0

if score == 7:
    print('U bent aangenomen') 

elif score > 7:
    print('U bent aangenomen')

else:
    score < 7
    print('U bent nietD aangenomen')  




