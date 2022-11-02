from ast import While
from turtle import left
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
teller = 9
bewegen = True
while bewegen:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        print('geen blokje')
        bewegen = False
        robotArm.wait()
        
    else:
        for x in range(0,teller):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,teller):
            robotArm.moveLeft()
        teller -=1
       
robotArm.wait()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()