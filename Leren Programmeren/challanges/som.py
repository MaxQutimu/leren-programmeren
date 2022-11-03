
verandering = 0
i = 50
som = i + verandering

while i <= 999:
    if i == 1000:
        break
    print(i)
    verandering = verandering + 1
    i = som + i + verandering
print("einde")