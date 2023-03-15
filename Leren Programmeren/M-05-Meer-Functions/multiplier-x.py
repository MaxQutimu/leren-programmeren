
cijfer = int(input("Van welk getal wilt u de tafle zien? "))


def hello(c:int):
    for x in range(10):
        print(f"{x + 1} x {c} = {(x + 1) * c}")

hello(cijfer)
hello(3)
hello(7)