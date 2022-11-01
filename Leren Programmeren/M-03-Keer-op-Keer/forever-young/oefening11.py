from turtle import left
from RobotArm import RobotArm

# Jouw python instructies zet je vanaf hier:
robotArm = RobotArm('exercise 11')
for i in range(0, 8):
    robotArm.moveRight()
for i in range(0, 9):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()
robotArm.wait()