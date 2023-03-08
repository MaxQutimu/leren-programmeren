aantal = int(input("typ hoeveel keer je fibonacci wilt doen? "))
nummer1, nummer2 = 0, 1
teller = 0
if aantal <= 0:
   print("voeg juiste cijfer in ")
elif aantal == 1:
   print("Fibonacci",aantal,":")
   print(nummer1)
else:
   print("Fibonacci:")
   while teller < aantal:
       print(nummer1)
       nextnummer = nummer1 + nummer2
       nummer1 = nummer2
       nummer2 = nextnummer
       teller += 1