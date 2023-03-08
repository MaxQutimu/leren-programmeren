mainCharacter = {
    'name' : 'luffy',
    'ownsHorse' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 2,
        'gold' : 1,
        'silver' : 7,
        'copper' : 25
    }
}
def copper2silver(amount:int) -> float:
    while mainCharacter['cash']['copper'] >= 10:
        mainCharacter['cash']['copper'] -= 10
        mainCharacter['cash']['silver'] += 1
    return mainCharacter['cash']
    pass    
copper2silver(1)

def silver2gold(amount:int) -> float:
    while mainCharacter['cash']['silver'] >= 5:
            mainCharacter['cash']['silver'] -= 5
            mainCharacter['cash']['gold'] += 1
    return mainCharacter['cash']
    pass
silver2gold(1)
def copper2gold(amount:int) -> float:
    while mainCharacter['cash']['copper'] >= 50:
            mainCharacter['cash']['copper'] -= 10
            mainCharacter['cash']['silver'] += 1
            silver2gold()
    return mainCharacter['cash']
    pass

def platinum2gold(amount:int) -> float:
    while mainCharacter['cash']['platinum'] >= 1:
            mainCharacter['cash']['platinum'] -= 1
            mainCharacter['cash']['gold'] += 25
    return mainCharacter['cash']
    pass
platinum2gold(1)
def getPersonCashInGold(personCash:dict) -> float:
    copper2silver(1)
    silver2gold(1)
    platinum2gold(1)
    return mainCharacter['cash']
    pass


print(mainCharacter['cash'])