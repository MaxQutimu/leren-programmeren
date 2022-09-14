from operator import truediv
from zipfile import LargeZipFile


print("Welkom in Pizza shop")
small=8.99
medium=10.99
large=13.99
var = 0
while var == 0:
    try:
        smallsizepizza=int(input("Hoeveel kleine pizza's wilt u?"))
    except:
        print('onjuiste ingewoerde waarde')
    var = +1
while var == 1:
    try:
        mediumsizepizza=int(input("Hoeveel medium pizza's wilt u?"))
    except:
        print('onjuiste ingewoerde waarde')
    var = +2
while var == 2:
    try:
        largesizepizza=int(input("Hoeveel groot pizza's wilt u?"))
    except:
        print('onjuiste ingewoerde waarde')
    var = +3
    

smallsizepizzaprize = smallsizepizza * small
mediumsizepizzaprize = mediumsizepizza * medium
largesizepizzaprize = largesizepizza * large

totaal = smallsizepizza * small + mediumsizepizza * medium + largesizepizza * large
var = 3
print(f'''uw heeft {smallsizepizza} small pizza's, {mediumsizepizza} medium pizza's, {largesizepizza} Grote pizza's besteld, uw totaal is {totaal} euro ''')
print(f'''|-----------------------------------------------------|
|                        Bon                          |
|                                                     |
|Small pizza {smallsizepizza} x {small}                           {smallsizepizzaprize} | 
|                                                     |
|Medium pizza {mediumsizepizza} x {medium}                         {mediumsizepizzaprize} |
|                                                     |
|Large pizza {largesizepizza} x { large}                          {largesizepizzaprize} |
|                                                     |
|                                              Totaal |
|                                              {totaal} |
|-----------------------------------------------------|''')


