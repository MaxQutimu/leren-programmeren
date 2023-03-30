import time
import math
from termcolor import colored
from data import *


##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount /10
    pass 
    

def silver2gold(amount:int) -> float:
    return amount / 5
    pass 

def copper2gold(amount:int) -> float:
    value = copper2silver(amount)
    return silver2gold(value)
    pass
    

def platinum2gold(amount:int) -> float:
    return amount * 25
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
    cost = (cost * JOURNEY_IN_DAYS)
    total = copper2gold(cost)
    return total
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
    lst = getShareWithFriends(friends)
    lst = getAdventuringPeople(lst)
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
    lst = []
    for item in items:
        Alle_item = f"{item['amount']}{item['unit']} {item['name']}"
        lst.append(Alle_item)
    return ', '.join(lst)

def getItemsValueInGold(items:list) -> float:
    value = 0
    for item in items:
        ValueItem = item['amount'] * item['price']['amount']
        if item['price']['type'] == 'copper':
            value += copper2gold(ValueItem)
        elif item['price']['type'] == 'silver':
            value += silver2gold(ValueItem)
        elif item['price']['type'] == 'gold':
            value += ValueItem
        elif item['price']['type'] == 'platinum':
            value += platinum2gold(ValueItem)
    return value
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
        total_gold = 0
        for money in people:
            s2g = money['cash']['silver']
            silver2gold(s2g)
            c2g = money['cash']['copper']
            copper2gold(c2g)
            p2g = money['cash']['platinum']
            platinum2gold(p2g)
            gold = money['cash']['gold']
            total_gold +=  platinum2gold(p2g) + silver2gold(s2g) + copper2gold(c2g) + gold
        return total_gold
    

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    lst = []
    for invest in investors:
        if invest['profitReturn'] <= 10:
            lst.append(invest)
    return lst

def getAdventuringInvestors(investors:list) -> list:
    lstAdventuring = []
    for people in getInterestingInvestors(investors):
        if people['adventuring']:
            lstAdventuring.append(people)
    return lstAdventuring

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totalCosts = 0

    adventuringInvestors = getAdventuringInvestors(investors)

    for investor in adventuringInvestors:
        totalCosts += getItemsValueInGold(gear)

    investorJourneyCosts = getJourneyFoodCostsInGold(len(adventuringInvestors), len(adventuringInvestors))
    investorRentalCosts = getTotalRentalCost(len(adventuringInvestors), len(adventuringInvestors))
    
    totalCosts += investorJourneyCosts + investorRentalCosts
    return totalCosts

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    
    humanInnCosts = silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT)
    horseInnCosts = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)
    total = (leftoverGold / (humanInnCosts + horseInnCosts))
    print(total)
    return total

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    humanInnCosts = silver2gold(people * COST_INN_HUMAN_SILVER_PER_NIGHT)
    horseInnCosts = copper2gold(horses * COST_INN_HORSE_COPPER_PER_NIGHT)

    return round(nightsInInn * (humanInnCosts + horseInnCosts), 2)
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


