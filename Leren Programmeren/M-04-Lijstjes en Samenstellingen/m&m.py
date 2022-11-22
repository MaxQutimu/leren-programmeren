import random
Kleuren = ("oranje","blauw","groen","bruin")
HoeveelHeidMM = int(input("Hoeveel M&M's er aan de zak toegevoegd moeten worden"))
ZakMetMM = []
for x in range(HoeveelHeidMM):
    ZakMetMM += random.choices(Kleuren)

print(ZakMetMM)