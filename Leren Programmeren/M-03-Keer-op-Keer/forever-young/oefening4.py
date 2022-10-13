from turtle import left
from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for right in range(5):
    robotArm.grab()
    for moveright in range(1):
        robotArm.moveRight()
        robotArm.drop()
    for m in range(1):
        robotArm.moveLeft()
for i in range(1):
    robotArm.moveRight()
for i in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()