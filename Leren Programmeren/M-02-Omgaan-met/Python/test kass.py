geel = input("Is de kaas geel?")

if geel == "Nee":
    schimmel = input("heeft de kaas blauwe schimmel?")

    if schimmel == "Ja":
        korst = input("heeft de kaas een korst? (Y/N)")

        if korst == "Ja":
            print("Blue de Rochbaron")
        
        else:
            print("Foume d'Ambert")
    
    else:
        korst1 = input("heeft de kaas een korst?")

        if korst1 == "Ja":
            print("Camembert")
        
        else:
            print("Mozzarella")

if geel == "Ja":
    gaten = input("Zitten er gaten in?")

    if gaten == "Ja":
        duur = input("Is de kaas belachelijk duur?")

        if duur == "Ja":
            print("Emmenthaler")
        
        else:
            print("Leerdammer")
    
    else:
        steen = input("Is de kaas hard als steen?")

        if steen == "Ja":
            print("Parmigiano Reggiano")
        
        else:
            print("Goudse kaas")