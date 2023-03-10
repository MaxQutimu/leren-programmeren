from operator import itemgetter

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

JOURNEY_IN_DAYS = 11
COST_FOOD_HUMAN_COPPER_PER_DAY = 4
COST_FOOD_HORSE_COPPER_PER_DAY = 3

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
        return coins
    pass


lestDictionairy1 = {
    'platinum' : 1,
    'gold' : 1,
    'silver' : 1,
    'copper' : 1
}
getPersonCashInGold(lestDictionairy1)

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    food_for_people = COST_FOOD_HUMAN_COPPER_PER_DAY  * people
    food_for_horses = COST_FOOD_HORSE_COPPER_PER_DAY * horses
    cost = food_for_people + food_for_horses
    cost = (cost * JOURNEY_IN_DAYS) / 50
    return cost
    pass

getJourneyFoodCostsInGold(12,3)


def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    
    pass
thingsList = [
    {
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }
]

result1 = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    }, {
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]

if getFromListByKeyIs(thingsList, 'round', True) != result1:
    print(False)