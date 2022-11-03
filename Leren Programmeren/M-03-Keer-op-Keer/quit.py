
herhaling = True
i = 0
lijst = ["yes","y","quit","ja","j"]

while herhaling:
    quit = input("Do you want to quit? ").lower()
    if quit in lijst:
        print("Bedankt voor je tijd")
        print(f"Vraag was {i} gesteld")

        herhaling = False
    
    else:
        i += 1
    
        

        