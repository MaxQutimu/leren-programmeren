print("Welkom in Pizza shop")
small=float(8.99)
medium=float(10.99)
Big=float(13.99)

smallsizepizza=int(input("Hoeveel kleine pizza's wilt u?"))
mediumsizepizza=int(input("Hoeveel medium pizza's wilt u?"))
bigsizepizza=int(input("Hoeveel groot pizza's wilt u?"))

totaal = smallsizepizza * small + mediumsizepizza * medium + bigsizepizza * Big

print(f'''uw heeft {smallsizepizza} small pizza's, {mediumsizepizza} medium pizza's, {bigsizepizza} Grote pizza's besteld, uw totaal is {totaal} euro ''')