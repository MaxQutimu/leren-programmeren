from sys import getallocatedblocks


while True:
    try:
        getal = int(input('Vul een getal in '))
        for x in range(1,11):
            print(f'{getal} x {x} = {x * getal}' )
    except:
        print('Vul juiste getal er in')