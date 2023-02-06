def hello():
    cijfer = int(input("Van welk getal wilt u de tafle zien? "))
    for x in range(10):
        print(f"{x + 1} x {cijfer} = {(x + 1) * cijfer}")

hello()
