herhaling = True
i = 0
while herhaling:
    quit = input("Do you want to quit? ").lower
    if quit in ["yes","y","quit","ja","j"]:
        print("Bedankt voor je tijd")
        print(f"Vraag was {i} gesteld")

        herhaling = False
    elif quit == "Quit":
        print("test")
    else:
        i += 1
        print(i)