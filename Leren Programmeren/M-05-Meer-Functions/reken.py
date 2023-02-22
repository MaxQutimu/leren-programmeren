
n1 = False

while True:
        if n1 == False:
         pass
        else:
            print(f'Wat wil je doen met jou getal {n1}')
    
        print('A - optellen')
        print('B - aftrekken')
        print('C - vermenigvuldigen')
        print('D - delen')
        print('E - ophogen')
        print('F - verlagen')
        print('G - verdubbelen')
        print('H - halveren')
        print('I - niks')
        keuze = input('kies een optie ').lower()
        if keuze == 'a' or 'b' or 'c' or 'd':
            if n1 == False:
                n1 = float(input('voeg 1 getal in'))
                
                n2 = float(input('voeg 2 getal in'))
            else:
                n2 = input('voeg 2 getal in')
            
            if keuze == 'a':
                n1 = n1 + n2
                print(n1)
            elif keuze == 'b':
                n1 = n1 - n2
                print(n1)
            elif keuze == 'c':
                n1 = n1 * n2
                print(n1)
            elif keuze == 'd':
                n1 = n1 / n2
                print(n1)
        elif keuze == 'e' or 'f' or 'g' or 'h':
            if n1 == False:
                n1 = float(input('voeg 1 getal in'))
                n2 = float(input('voeg 2 getal in'))
            else:
                n2 = input('voeg 2 getal in')
                
            if keuze == 'e':
                n1 = n1 + 1
                print(n1)
            elif keuze == 'f':
                n1 = n1 - 1
                print(n1)
            elif keuze == 'g':
                n1 = n1 * 2
                print(n1)
            elif keuze == 'h':
                n1 = n1 / 2
                print(n1)
        
                
        elif keuze == 'i':
            print('Dank je voor het gebruik')
            break
        else:
            print('voeg juiste keuze in')