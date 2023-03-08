mainCharacter = {
    'name' : 'Luffy',
    'ownsHorse' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 2,
        'gold' : 1,
        'silver' : 10,
        'copper' : 233
    }
}
# copper - silver ratio 10:1
def copper2silver(amount:int) -> float:
    silver = amount / 10
    return silver
    pass 
    

def silver2gold(amount:int) -> float:
    gold = amount / 5
    return gold
    pass 

def copper2gold(amount:int) -> float:
    gold = amount / 50
    return gold
    pass
    

def platinum2gold(amount:int) -> float:
    gold = amount * 25
    return gold
    pass


print(mainCharacter['cash'])
def getPersonCashInGold(personCash:dict) -> float:
    total_gold = 0.0
    for coins in personCash:
        s2g = personCash['silver']
        silver2gold(s2g)
        c2g = personCash['copper']
        copper2gold(c2g)
        p2g = personCash['platinum']
        platinum2gold(p2g)
        gold = personCash['gold']
        total_gold =  platinum2gold(p2g) + silver2gold(s2g) + copper2gold(c2g) + gold
        print(total_gold)
        return coins
    pass


lestDictionairy1 = {
    'platinum' : 1,
    'gold' : 1,
    'silver' : 1,
    'copper' : 1
}
getPersonCashInGold(lestDictionairy1)