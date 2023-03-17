import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY 
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY

##################### M04.D02.O2 #####################

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
        return total_gold
    pass

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    food_for_people = COST_FOOD_HUMAN_COPPER_PER_DAY  * people
    food_for_horses = COST_FOOD_HORSE_COPPER_PER_DAY * horses
    cost = food_for_people + food_for_horses
    cost = (cost * JOURNEY_IN_DAYS) / 50
    return cost
    pass

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lst = []
    for x in range(len(list)):
        if list[x][key] == value:
            lst.append(list[x])
    return lst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    lst = []
    for x in range(len(friends)):
        if friends[x]['adventuring'] and friends[x]['shareWith']:
            lst.append(friends[x])
    return lst

##################### M04.D02.O6 #####################

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
    renttent = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7 )
    return silver2gold(renthorses) + renttent

    

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()


