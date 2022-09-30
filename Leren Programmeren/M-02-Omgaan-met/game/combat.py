
hero = {'name' : "Black Knight's of Arcadia",
        'lvl' : 1,
        'xp' : 0,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 500,
                'heal' : [4,8],
                'atk' :[20, 30] }}


goblin = {'name' : "Small group of Goblin's",
        'lvl' : 1,
        'xp' : 0,
        'reward' : 25,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 70,
                'heal' : [4,8],
                'atk' :[3, 5] }}


Asassins = {'name' : "Assassins",
        'lvl' : 1,
        'xp' : 0,
        'reward' : 25,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 150,
                'heal' : [4,8],
                'atk' :[8, 12] }}


Large_army = {'name' : "Large army of enemy's",
        'lvl' : 1,
        'xp' : 0,
        'reward' : 25,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 15000,
                'heal' : [4,8],
                'atk' :[200, 500] }}


Orc = {'name' : "Group of Orc's",
        'lvl' : 1,
        'xp' : 0,
        'reward' : 250,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 250,
                'heal' : [4,8],
                'atk' :[20, 30] }}

AmbushedDemon_king = {'name' : "Demon King",
        'lvl' : 1,
        'xp' : 0,
        'reward' : 25,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 350,
                'heal' : [4,8],
                'atk' :[20, 25] }}

Demon_king = {'name' : "Demon King",
        'lvl' : 1,
        'xp' : 0,
        'reward' : 25,
        'lvlNext' : 25,
        'stats' : {'str' : 1,
                'dex' : 1,
                'int' : 1,
                'hp' : 750,
                'heal' : [4,8],
                'atk' :[30, 35] }}

def level(hero):
    nStr, nDex, nInt = 0, 0, 0
    while hero['xp'] >= hero['lvlNext']:
        hero['lvl'] +=1
        hero['xp'] = hero['xp'] - hero ['lvlNext']
        hero['lvlNext'] = round(hero['lvlNext'] * 1.5)
        nStr += 1
        nDex += 1
        nInt += 1
    
    print('level:',hero['lvl']) #lvl
    # print('STR +{} DEX +{} INT +{}' .format(nStr, nDex, nInt)) #oude stats + nieuwe stats
    # print()
    print('STR {} +{} DEX {} +{} INT {} +{}'.format(hero['stats']['str'], nStr,
                                                    hero['stats']['dex'], nDex,
                                                    hero['stats']['int'], nInt,))
    
    hero['stats']['str'] += nStr
    hero['stats']['dex'] += nDex
    hero['stats']['int'] += nInt

from ast import If, Return
from cgi import test
from pstats import Stats
from random import randint, random

def takedmg(attacker, defender):
    dmg = randint(attacker['stats']['atk'][0], attacker['stats']['atk'][1])
    defender['stats']['hp'] = defender['stats']['hp'] - dmg
    if hero['stats']['hp'] <=0:
        print('You have been slaied')
        print('game over')
        exit(0)
    elif defender['stats']['hp'] <= 0:
        print('{} has been slain'.format(defender['name']))
        hero['xp'] += goblin['reward']
        level(hero)
        input('Press any key to go forward.')
        return False
    elif defender['stats']['hp'] > 0 and hero['stats']['hp'] > 0:
        print('{} takes {} damage!' . format(defender['name'], dmg))

def takeheal(attacker, defender):
    heal = randint(attacker['stats']['heal'][0], attacker['stats']['heal'][1])
    defender['stats']['hp'] = defender['stats']['hp'] + heal
    if defender['stats']['hp'] <= 0:
        return False  
    else:
        print('{} heal {} !' . format(defender['name'], heal))

def show_hp(attacker, defender):
    show_hp_all = (attacker['stats']['hp']) 
    defender['stats']['hp']  = defender['stats']['hp']
    if defender['stats']['hp'] <= 0:
        return False 
    else:
        print('{} hp left '.format(defender['stats']['hp'], show_hp_all))
        return True

def commands(player, enemy):
    while True:
        if enemy['stats']['hp'] <=0:
            break
        elif enemy['stats']['hp'] >0:
            while enemy['stats']['hp'] >0:    
                print('-----------------------------------------------')
                cmd = input('Do you want to attack, heal of run? ').lower()
                if 'attack' in cmd:
                    kansCrt = randint(0,17)
                    if kansCrt in (15,16):
                        print('Your hit was critical damage x3')
                        takedmg(player, enemy)
                        if enemy ['stats']['hp'] >0:
                            takedmg(player, enemy)
                            if enemy ['stats']['hp'] >0:
                                takedmg(player, enemy)
                            else:
                                pass
                        else:
                            pass
                        show_hp(player,enemy)
                    elif kansCrt == 14:
                        takedmg(player, enemy)
                        show_hp(player,enemy)
                        print('While swinging you got hit by a arrow: damage taken x2')
                        takedmg(enemy, player)
                        takedmg(enemy, player)
                        show_hp(enemy,player)
                        
                    elif kansCrt in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,17):
                        takedmg(enemy, player)
                        show_hp(enemy,player)
                        
                        takedmg(player, enemy)
                        show_hp(player,enemy)
                        
                        

                elif 'run' in cmd:
                    print('{} takes the opportunity to attack!'.format(enemy['name']))
                    takedmg(enemy, player)
                    show_hp(enemy,player)
                    show_hp(player,enemy)
                elif 'heal' in cmd:
                    if hero['stats']['hp'] >=500:
                        print('You caný heal anymore you hp is full')
                    else:
                        kans = randint(0,11) 
                        if kans in (9,10):
                            takeheal(enemy, player)
                            print('{} takes the opportunity to attack!'.format(enemy['name']))
                            takedmg(enemy, player)
                            show_hp(enemy,player)
                        elif kans == 8:
                            print('You got blessed healing x2')
                            takeheal(enemy, player)
                            takeheal(enemy, player)
                            show_hp(enemy,player)
                    
                        else:
                            takeheal(enemy, player)
                            show_hp(enemy,player)
                
                else:
                    print('Unknown command: commands - attack/heal/run')
                    
            




