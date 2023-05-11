opgeslagen = {"bolletjes": 0 ,
          "hoorntje_bakje":{"bakje":0,
                           "hoornje":0}}   
def vraag_bolletjes():
    while True:

        bolletjes = int(input("aantal bolletjes "))
        if bolletjes == 0:
            print('Vul getal groter dan 0')
        elif bolletjes <= 8:
            break 
        elif bolletjes >= 8:
            print('Sorry, zulke grotebakken hebben we niet')
        else:
            print('Sorry ik snap het niet')
    return bolletjes

def vraag_bakje(bolletjes):
    hoorntje_of_bakje = 'bakje'
    if bolletjes <= 3:
            while True:
                hoorntje_of_bakje = input(f'Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje? ')
                if hoorntje_of_bakje == 'hoorntje' or 'baakje' :
                    break
                else:
                    print('sorry ik snap het niet')
    return hoorntje_of_bakje

def opslag(bolletjes , hoorntje_of_bakje):
    opgeslagen["bolletjes"] =+ bolletjes
    opgeslagen["hoorntje_bakje"][hoorntje_of_bakje] =+ 1
    return opgeslagen
                    
def meer_bestellen():
    while True:
        meer = input('Wilt u meer bestelen? ')
        if meer in ["ja","nee"]:
            break
        else:
            print('Ik snap het niet')
    return meer

while True:
    bolletjes = vraag_bolletjes()
    hoorntje_of_bakje = vraag_bakje(bolletjes)
    opgeslegen = opslag(bolletjes, hoorntje_of_bakje)
    verder = meer_bestellen()
    if verder == "nee":
        break

print(opgeslegen)








