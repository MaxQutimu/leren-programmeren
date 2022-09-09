from re import A


nummer1 = float(input('Voel eerste nummer in'))
nummer2 = float(input('Voel tweede nummer in'))

if   (nummer1>nummer2):
    largest = nummer1
    smallest = nummer2
    print(f'''nummer a  {nummer1} is groter dan nummer b {nummer2}''')
    print('Grootste nummer is',largest)
    print('Kleinste nummer is',smallest)

elif (nummer1<nummer2):
    largest = nummer2
    smallest = nummer1

    print(f'''nummer a  {nummer1} is kleiner dan nummer b {nummer2}''')
    print('Grootste nummer is',largest)
    print('Kleinste nummer is',smallest)

else :
    gelijk = nummer1 , nummer2

    print(f'''nummer a {nummer1} en nummer b {nummer2} zijn geijk''')
    print('Grootste nummer is',gelijk)





