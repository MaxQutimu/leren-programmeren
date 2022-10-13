from turtle import left
from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for x in range(7):
    robotArm.moveRight()
for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if i < 7:
        for x in range(2):
            robotArm.moveLeft()
    






# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()