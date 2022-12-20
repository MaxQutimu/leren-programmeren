import random
Kaarten = ("2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas")
Kleur = ("harten ","klaveren ","schoppen ","ruiten ")
Deck = []
teller = 0
for x in Kleur[0:4]:
    for i in Kaarten[0:13]:
        Deck.append (x + i)
Deck.append ("Joker1")
Deck.append ("Joker2")
for y in range(7):
    RandomKaart= random.choices(Deck)
    teller += 1
    print(f"Karten {teller} : {RandomKaart}")

print(Deck)