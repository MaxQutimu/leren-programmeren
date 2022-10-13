from shutil import move
from turtle import left
from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed= 5
for x in range(5):
    robotArm.moveRight()
    for i in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()

    robotArm.moveRight()
            



    






# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()