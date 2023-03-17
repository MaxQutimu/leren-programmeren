from operator import itemgetter
import math
from functions import print_colorvars

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
COST_TENT_GOLD_PER_WEEK = 3
COST_HORSE_SILVER_PER_DAY = 5

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



def getNumberOfHorsesNeeded(people:int) -> int:
    horses = people / 2 
    roundhorses = math.ceil(horses)
    return roundhorses

def getNumberOfTentsNeeded(people:int) -> int:
    tents = people / 3
    roundtents = math.ceil(tents)
    return roundtents
    

def getTotalRentalCost(horses:int, tents:int) -> float:
    renthorses = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    renttent = tents * (COST_TENT_GOLD_PER_WEEK * 5 / 7) * round(JOURNEY_IN_DAYS,7)
    totalrent = (renthorses  + renttent) 
    print(totalrent)
    return totalrent



if getNumberOfTentsNeeded(6) != 2:
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')

if getTotalRentalCost(1,2) != 23.0:
    print_colorvars(vars=['Test 6 is False'], color='red')
else:
    print_colorvars(vars=['Test 6 is correct'], color='green')

if getTotalRentalCost(5,2) != 67.0:
    print_colorvars(vars=['Test 7 is False'], color='red')
else:
    print_colorvars(vars=['Test 7 is correct'], color='green')

if getTotalRentalCost(3,11) != 99.0:
    print_colorvars(vars=['Test 8 is False'], color='red')
else:
    print_colorvars(vars=['Test 8 is correct'], color='green')