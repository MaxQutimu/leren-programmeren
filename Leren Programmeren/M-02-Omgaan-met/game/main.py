from faulthandler import cancel_dump_traceback_later
from unicodedata import name
from ast import Break
from asyncio import events
from socket import herror
import string
import sys
from random import randint
import time
def print_delay(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
import intro
import castel
import kings_hall_1dialog
import Kings_hall_2dialog
from time import sleep
from turtle import Turtle, delay
time.sleep(4)


while True:
    einde_1 = input('Are gonna help your king? Yes/No ').lower()
    if einde_1 in ('no','n','nee'):
        import gilotine
        print_delay('You betrayed your king and lost your head \n')
        time.sleep
        print_delay('Game Over')
        exit(0)
    elif einde_1 in ('yes','y','ja','j','ye'):
        break
    else:
        print("use something")


print_delay("After a king's invitations\n")
print_delay("Black knight of Arcadia with their Commander up front begon journey to defeat Demon king\n")
time.sleep(3)
print_delay("Their first stop was in a tavern, 1 day on foot travel from capital\n")
print_delay("While in tavern:\n")
import tavern
time.sleep(2)
import tavern_dialog_1
time.sleep(3)
import tavern_dialog_2
time.sleep(2)
print_delay("You : Beer for my whole company\n")
time.sleep(1)
print_delay("Tavernkeeper: Are you perhaps the legendary commander... :\n")
time.sleep(1)
while True:
    naam = input("'What's your name?'")
    if naam == '':
        print('Fill your name in!')
    else:
        break
time.sleep(1)
print_delay(f"Tavernkeeper:{naam} of the Black knights?\n")
time.sleep(1)
print_delay("Tavernkeeper:It's honor to host you and your company\n")
time.sleep(2)
print_delay("After some time you and your company headed toward the enemy\n")
time.sleep(3)
print_delay("After a 2 day a whole company encountered a first forces of enemy\n")
time.sleep(2)
print_delay("Scout: Commander we scouted small group of goblins\n")
time.sleep(2)
print_delay("You : Troops prepare for fight!\n")
time.sleep(2)
import knight
print_delay("You encounterd Group of Goblin's\n")
time.sleep(2)
import combat

combat.commands(combat.hero, combat.goblin) 


print_delay("Soldier:Commander we won with small loses\n")
time.sleep(2)
import Knight_on_horse
print_delay("You: troops gather up we are heding to The Realm of Chaos!\n")
print_delay("After hours of march night have fallen\n")
while True:
    camp = input("Soldier: Commander should we camp here? Yes/No ").lower()
    if camp in ('yes','y','ja','j'):
        import campfire
        print_delay("Soldier: Commander we are being ambushed!\n")
        print_delay("You: Troops prepare for combat!\n")
        print_delay("You encountered Asassins\n")
        combat.commands (combat.hero, combat.Asassins)
        break

    elif camp in ('no','n','nee'):
        print_delay("You decited to go in the night\n")
        print_delay("Your troops are exhausted\n")
        print_delay("You army was abushed by Large army of enemy\n")
        combat.commands(combat.hero, combat.Large_army)
        break
    else:
        print('Please type in "Y" / "N"')
    


print_delay("Solier: Commander we won!\n")
time.sleep(2)
print_delay("Scout: Sir we scouted a cave ahead should we try to take cover and rest there?\n")
time.sleep(2)
print_delay("You:Troop's move out!\n")
time.sleep(2)
print_delay("It looks like a dungeon\n")
print_delay("Ground begon to shake\n")
print_delay("The entrnce collapsed\n")
print_delay("You: It looks like we need to go deeper\n")
print_delay("Soldier: Enemy ahead!\n")
print_delay("You encountred group Orc's\n")
while True:
    sneak = input("Do you try to sneak around orc's? Yes/No ").lower()
    if sneak in ("ja","yes","y","j","je"):
        sneakchance = randint(0,1)
        if sneakchance == 1:
            print_delay("You failed to sneak around orc's\n")
            print_delay("Prepare for fight!\n")
            combat.commands(combat.hero,combat.Orc)

            break
        else:
            break
    elif sneak in ("no","n","nee"):
        print_delay("You decited to fight group of Orc's!\n")
        combat.commands(combat.hero,combat.Orc)
        break

    else:
        print('Please type in "Y" / "N"')

print_delay("Soldier:Sir look we can see light at the end of the tunnel!\n")
print_delay("You and your company exited the tunnel\n")
print_delay("You hear horses stepping\n")
print_delay("You see some knight riding toward's you\n")
print_delay("Knight's of the Holy Order look's at your banner\n")
print_delay("Knight's of the Holy Order got off their horses and knelt before you\n")
print_delay(f"Knight of the Holy Order: We welcome commander {naam} of Black Knight's\n")
print_delay("Knight of the Holy Order: Sir we will take you to the pope\n")
import holyorder
print_delay("You went inside castle\n")
List_Event_Yes_No = ('yes','y','ye','j','ja','no','n','nee',)
List_Event_True_Lie = ('truth','tru','true','t','lie','lies','l')

def Question(promt: str, opties: list) -> str:
    antowoord = ""
    while antowoord not in opties:
        antowoord = input(promt+"\n")
        if antowoord not in opties:
            print()
    return antowoord
while True:
    event = Question("Do you kneel before? Y/N ",List_Event_Yes_No).lower()
    if event in ('yes','y','ye','j','Ja'):
        print_delay("You knelt before pope\n")
        print_delay("You:Commander of black knight's welcom his holines pope\n")
        print_delay("Pope: Stand up Commander\n")
        print_delay("Pope: What is commander of black knight's doing in holy states?\n")
        event_2 = Question("Do you tell pope truth? Truth / Lie ",List_Event_True_Lie).lower()
        if event_2 in ('truth','true','t','waar','waarheid','tru'):
                print_delay("Pope: I see in that case i will help you\n")
                print_delay("Pope: Bring the sword\n")
                print_delay("Servant of pope: Yes your holines\n")
                print_delay("Pope: I the pope of holy states bless you with the gift you this Holy sword\n")
                event_3_blesing = Question("Do you accept blessing? (extra XP + DMG) Y/N ",List_Event_Yes_No).lower()
                if event_3_blesing in ('yes','y','j','ja'):
                        print("You gained god's belssing\n")
                        print("You gained new weapon : Holy Sword")
                        combat.hero['xp'] +100
                        combat.hero['stats']['atk'][0] += 25
                        combat.hero['stats']['atk'][1] += 25
                        combat.hero['stats']['heal'][0] += 8
                        combat.hero['stats']['heal'][1] += 12
                        combat.hero['stats']['hp'] == 500
                        print('+100xp + extra dmg + extra healing + fully healed')
                        print("New Stats:")
                        print("DMG = 20/30 -> 45/55")
                        print("Heal = 4/8 -> 12/20")
                        print("Fully healed")
                        break
                elif event_3_blesing in ('no','n','nee'):
                        print("Pope: I understand\n")
                        print("Pope: I still wish to take this sword\n")
                        combat.hero['stats']['atk'][0] += 5
                        combat.hero['stats']['atk'][1] += 5
                        print("+5 dmg")
                        print_delay("New stats:")
                        print("DMG = 20/30 -> 25/35")
                        break
                
        elif event_2 in ('lie','lies','not true','l'):
                print_delay("You:We are heading to kingdom of Argon\n")
                print_delay("Pope: Fareware you may go now\n")
                break
    elif event in ('no','n','Nee',):
        print_delay("Pope: What is commander of black knight's doing in holy states?\n")
    
        event_2_alt = Question("Do you tell pope truth? Truth / Lie ",List_Event_True_Lie).lower()
        if event_2_alt in ('truth','true','t','waar','waarheid','tru'):
                print_delay("Pope: In that case i will help you\n")
                print_delay("Your company got healed\n")
                combat.hero['stats']['hp'] == 500
                print("fully healed hp = 500")
                break
        elif event_2 in ('lie','lies','not true','l'):
                print_delay("You:We are heading to kingdom of Argon\n")
                print_delay("Pope: Fareware you may go now\n")
                break
    

print_delay("Knight's of the Holy Order escorted you from Holy states\n")
print_delay("You and you company headed towards the Realm of Chaos\n")
print_delay("After a couple days of march\n")
print_delay("Scouts:Sir we scouted a army of demon king\n")
Ambush_demon_king= Question("Should we ambush the enemy? Y/N ",List_Event_Yes_No).lower()
if Ambush_demon_king in ("ja","j","y","yes","ye"):
    AmbushChance= randint(0,1)
    if AmbushChance == 1:
        print_delay("Your abush was succesful\n")
        print_delay("You encountered Demon King and his army!\n")
        print_delay("Because of you ambush enemy army sufered debuff\n")
        combat.commands(combat.hero,combat.AmbushedDemon_king)
    elif AmbushChance == 0:
        print_delay("Your ambush was unsuccesful\n")
        print_delay("You encoutered Demon King and his army!\n")
        combat.commands(combat.hero,combat.Demon_king)
        
elif Ambush_demon_king in ("no","n","nee"):
    print_delay("You encoutered Demon King and his army!\n")
    combat.commands(combat.hero,combat.Demon_king)

print_delay("You slaied Demon King!\n")

print('''
 __     __ ____   _    _  __          __ ____   _   _ 
 \ \   / // __ \ | |  | | \ \        / // __ \ | \ | |
  \ \_/ /| |  | || |  | |  \ \  /\  / /| |  | ||  \| |
   \   / | |  | || |  | |   \ \/  \/ / | |  | || . ` |
    | |  | |__| || |__| |    \  /\  /  | |__| || |\  |
    |_|   \____/  \____/      \/  \/    \____/ |_| \_|
''')





