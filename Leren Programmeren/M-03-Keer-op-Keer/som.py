
verandering = 0
cijfer = 50
som = cijfer + verandering

while cijfer <= 9999:
    if cijfer >= 1100:
        break
    print(cijfer)
    verandering = verandering + 1
    cijfer = som + cijfer + verandering
print("end")