iPhone =  int(input('hoe duur is het iPhone?'))
Samsung = int(input('hoe duur is het samsung?'))
prijs_verschill_iphone_duurder = iPhone - Samsung
prijs_verschill_samsung_duurder = Samsung - iPhone

if  iPhone < Samsung:
    print(f'De Samsung is duurst, de telefoon kost: {Samsung}')
    print(f'De iPhone is goedkoopst, de telefoon kost: {iPhone}')
    
    if iPhone - Samsung < 50:
        print(f'Het advies is dus de iPhone te kopen. Deze is namelijk {prijs_verschill_samsung_duurder} euro Goedkoper')
    elif iPhone - Samsung > 50:
        print(f'Het advies is dus de iPhone te kopen. Deze is namelijk {prijs_verschill_samsung_duurder} euro Duurder')
    elif iPhone - Samsung == 50:
        print(f'Het advies is dus de iPhone te kopen. Deze is namelijk {prijs_verschill_iphone_duurder} euro duurder dan de Samsung')
        


elif  iPhone > Samsung:
    print(f'De iPhone is duurst, de telefoon kost: {iPhone}')
    print(f'De Samunsg is goedkoopst, de telefoon kost: {Samsung}')
    
    if iPhone - Samsung < 50:
        print(f'Het advies is dus de iPhone te kopen. Deze is namelijk {prijs_verschill_iphone_duurder} euro duurder dan de Samsung')
    elif iPhone - Samsung > 50:
        print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {prijs_verschill_iphone_duurder} euro goedkoper dan de iPhone')
    elif iPhone - Samsung == 50:
        print(f'Het advies is dus de iPhone te kopen. Deze is namelijk {prijs_verschill_iphone_duurder} euro duurder dan de Samsung')


elif iPhone == Samsung:
    print(f'Het advies is dus de iPhone te kopen. Deze is namelijk zelfde prijs als een Samsung')

else:pass

