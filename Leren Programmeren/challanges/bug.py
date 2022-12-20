Naam = int(input("Wat is je naam"))

a = int(input("Eerste cijfer"))
b = int(input("Tweede cijfer"))

a = b

loop = True


while loop:
    if a != b :
        print("{naam} :Eerste cijfer is {A} Tweede cijfer is {B}")
        print("That's it")
        loop = False
    elif a == b:
        print("Eerste cijfer is {A} Tweede cijfer is {B}")
        print("I don't want this answer")
    else:
        print("Error")
        break

print("Congratulations")




