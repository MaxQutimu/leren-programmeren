from turtle import left
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
# robotArm.speed = 5
moves = 8
robotArm.grab()
for z in range(4):
    for x in range(moves):
        robotArm.moveRight()   
    robotArm.drop()
    moves = moves - 1
    for i in range(moves):
        robotArm.moveLeft()
    if z < 3:
        robotArm.grab()
    moves = moves - 1
    

     
        
    

    






# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()