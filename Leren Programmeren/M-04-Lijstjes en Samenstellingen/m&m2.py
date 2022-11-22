import random
kleuren = ("groen", "blauw","oranje","bruin")
# hoeveel = int(input("hoeveel mms wil je?"))
bowl ={} 
while True:
    try:
        hoeveel = int(input("hoeveel mms wil je?"))
        break
    except:
        print("voer geldig getal in")


for kleur in kleuren:
    bowl[kleur] = 0

for index in range(0, hoeveel):
    randomnummer = random.randint (0,len(kleuren)- 1)
    bowl[kleuren[randomnummer]] += 1

print(bowl)