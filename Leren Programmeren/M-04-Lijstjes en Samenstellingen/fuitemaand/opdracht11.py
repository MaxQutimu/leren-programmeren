from fruitmand import fruitmand
kleuren = []
for x in fruitmand:
    if x['color'] not in kleuren:
        kleuren.append(x['color'])
loop = True
while loop:
        kleur_input = input('Kies een kleur uit: yellow, green, orange, red, brown: ').lower()
        if kleur_input in kleuren:
            print(f'Gekozen kleur is {kleur_input}')
            loop = False
        else:
            print('Kies een juiste kleur')

rond,niet_rond = 0,0   
for i in range(len(fruitmand)):
    kleuren = fruitmand[i].get('color')
    if kleuren == kleur_input:
        if fruitmand[i].get('round'):
            rond += 1
        else:
            niet_rond += 1

if rond > niet_rond :
    print(f'Ronde fruiten: {rond} niet ronde fruiten: {niet_rond}')
    print(f'Er zijn meer ronde: {rond} fruiten dan niet ronde fruiten:{niet_rond}')
elif rond < niet_rond:
    print(f'Ronde fruiten: {rond} niet ronde fruitne: {niet_rond}')
    print(f'Er zijn meer niet ronde fruiten: {niet_rond} dan ronde fruiten: {rond}')
else:
    print(f'Ronde fruiten: {rond} niet ronde fruitne: {niet_rond}')
    print(f'Er zijn even veel ronde fruiten: {rond} als niet rone fruiten: {niet_rond}')

