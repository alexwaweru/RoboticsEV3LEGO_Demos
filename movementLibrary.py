#!/usr/bin/env python3

#author James Mureithi Mugo
#author Ukpong, Itoro Oluwasegun
#author Jennifer Sarfo 

import ev3dev.ev3 as ev3
import time

# Variables referring to the Motors
rightM = ev3.LargeMotor('outC')
leftM = ev3.LargeMotor('outB')

# Create a variable referring to the screen
lcd = ev3.Screen()

# Variables assigned to the measured values of PI, radius (of the motor), 
# and baseline drawn by the circumference made by the orbiting robot
PI = 3.142
r = 2.7
b = 12.3

# A function that facilitates driving straights given the distance and speed
def driveStraight(distance, speed):
  if(speed > 0 and speed <1000):
  #calculates the encoder ticks for the given distance
    n = (180 * distance)/ (PI * r)
    rightM.run_to_rel_pos(position_sp=n, speed_sp=speed, stop_action="brake")
    leftM.run_to_rel_pos(position_sp=n, speed_sp=speed, stop_action="brake")
    
    rightM.wait_while('running')
    leftM.wait_while('running')
    
  else:
    lcd.draw.text((20, 50),'Trying to drive too fast')
    lcd.update()
    time.sleep(5)

# A function that allows the robot to turn right at a given angle, and speed        
def turnRight(angle, speed):
  if(speed > 0 and speed < 1000):
  #calculates the encoder ticks for the given angle
    n = (b * angle)/ r
    leftM.run_to_rel_pos(position_sp=n, speed_sp=speed, stop_action="brake")
    rightM.stop()
    
    leftM.wait_while('running')
   
# A function that allows the robot to turn left at a given angle, and speed 
def turnLeft(angle, speed):
  if(speed > 0 and speed < 1000):
  #calculates the encoder ticks for the given angle
    n = (b * angle)/ r
    rightM.run_to_rel_pos(position_sp=n, speed_sp=speed, stop_action="brake")
    leftM.stop()
    
    rightM.wait_while('running')

# A function that allows the robot to spin right at a given angle, and speed 
def spinRight(angle, speed):
    #calculates the encoder ticks for the given angle
    n = (b * angle)/ r
    rightM.run_to_rel_pos(position_sp=-n, speed_sp= speed, stop_action="brake")
    leftM.run_to_rel_pos(position_sp=n, speed_sp= speed, stop_action="brake")
    
    rightM.wait_while('running')
    leftM.wait_while('running')

# A function that allows the robot to spin left at a given angle, and speed
def spinLeft(angle, speed):
    #calculates the encoder ticks for the given angle
    n = (b * angle)/ r
    rightM.run_to_rel_pos(position_sp=n, speed_sp= speed, stop_action="brake")
    leftM.run_to_rel_pos(position_sp=-n, speed_sp= speed, stop_action="brake")
    
    rightM.wait_while('running')
    leftM.wait_while('running')
    
def spinForever(spd):
    leftM.run_forever(speed_sp=-spd)
    rightM.run_forever(speed_sp=spd)
    
#    rightM.wait_while('running')
#    leftM.wait_while('running')
    
def brakeToStopDriving():
    rightM.stop()
    leftM.stop()
    
def driveForever(spd):
    rightM.run_forever(speed_sp= spd)
    leftM.run_forever(speed_sp= spd)
    
def turnRightForever():
    rightM.stop();
    leftM.run_forever(speed_sp= 100)
    
def turnLeftForever():
    rightM.run_forever(speed_sp= 100)
    leftM.stop()