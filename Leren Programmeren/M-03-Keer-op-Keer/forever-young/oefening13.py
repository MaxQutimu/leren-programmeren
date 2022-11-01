from turtle import left
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
teller = 9
tellerleft = 9
for x in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        robotArm.wait()
    else:
        for x in range(0,teller):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,tellerleft):
                robotArm.moveLeft()
    teller -=1
    tellerleft -=1
robotArm.wait()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()