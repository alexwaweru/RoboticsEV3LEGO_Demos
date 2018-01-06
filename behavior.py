#!/usr/bin/env python3
import math, random, ev3dev.ev3 as ev3
from movementLibrary import *
from threading import Thread

'''Initializing the lcd, buttons and motors as global variables'''
lcd = ev3.Screen()                   
rightMotor = ev3.LargeMotor('outC')  
leftMotor = ev3.LargeMotor('outB')   
button = ev3.Button()     

'''Connecting the camera and the ultra sonic sensor'''
camera = ev3.Sensor(address=ev3.INPUT_1)  
us = ev3.UltrasonicSensor()

'''Check whether the camera and the ultra sonic sensors have been connected'''
assert camera.connected, "Error while connecting Pixy camera to port 2"
assert us.connected, "Connect a single US sensor to any sensor port"

'''Setting the camera units'''
CAMERA_WIDTH_PIXELS = 255
CAMERA_HEIGHT_PIXELS = 255

'''Initializing Global variables used to switch between the sub-threads and the main thread'''
global seen_object
global search_for_object
global avoid_obstacle

seen_object = False
search_for_object = True
avoid_obstacle = True

'''Dimensions of the robot'''
PI = math.pi
r = 2.7 #Circumference of the robots wheels
b = 12.3 #Width of the robot

'''This method sets the camera for a specific color'''
def setCameraMode(sigNum):
    camera.mode = 'SIG'+str(sigNum)


'''This methods allows the robot to make a compelete revolution as it looks
    for a green object'''
def completeRevolution(angle=360, speed=100):
    #calculates the encoder ticks for the given angle
    n = (b * angle)/ r
    rightM.run_to_rel_pos(position_sp=-n, speed_sp= speed, stop_action="brake")
    leftM.run_to_rel_pos(position_sp=n, speed_sp= speed, stop_action="brake")
    
    rightM.wait_while('running')
    leftM.wait_while('running')
    
'''This methods prompts the robot to turn right and the default angle is 90'''
def turnRight(angle = 90, speed):
    if(speed > 0 and speed < 1000):
        #calculates the encoder ticks for the given angle
        n = (b * angle)/ r
        leftM.run_to_rel_pos(position_sp=n, speed_sp=speed, stop_action="brake")
        rightM.stop()
        leftM.wait_while('running')


'''This method prompts the robot to drive straight forever until thread is stopped'''
def driveForever(speed = 100): #default speed is 100 revs/sec
    rightM.run_forever(speed_sp= speed)
    leftM.run_forever(speed_sp= speed)

 
'''This method makes the robot spin in position or wander randomly
    until a green object comes into the field of view of the camera'''
def randomSearch():
    global seen_object
    global search_for_object
    global avoid_obstacle
    print("spinAndFind running")
    objCount = camera.value(0) # get the number of objects seen by the camera

    if (objCount > 0):    
        #If we see at least one object, stop the robot
        leftMotor.stop()
        rightMotor.stop()
        #Make a beep sound to notify that an object has been seen
        ev3.Sound.beep()
        #Set the seen_object and search_object global variables to True and False respectively
        seen_object = True
        search_for_object = False            
    else:
        #Let the object either spin in position or wander randomly
        choice = random.randint(1,2)
        if choice == 1:
            #Spin around in place
            completeRevolution()
        else:
            #Wander randomly
            if (camera.mode!=4 and distance<=20):
                avoid_obstacle = False
                leftMotor.run_forever(speed_sp = 100)
                rightMotor.run_forever(speed_sp = 100)
            else:
                avoid_obstacle = True


'''This method prompts the robot to appraoch the green object once the object
    comes within the field of view'''
def approach():
    global search_for_object
    print("Approach running")
    us.mode='US-DIST-CM'
    distance = us.value()/10
    print(distance)

    # get the position and dimensions of the largest object seen
    x = camera.value(1) # x coordinate of middle of largest object
    y = camera.value(2) # y coordinate of middle of largest object
    w = camera.value(3) # width of largest object
    h = camera.value(4) # height of largest object
    while seen_object:
        if (x < CAMERA_WIDTH_PIXELS/2 - w/2):
            leftMotor.run_forever(speed_sp=0)
            rightMotor.run_forever(speed_sp=100)        
        elif (x > CAMERA_WIDTH_PIXELS/2 + w/2):
            leftMotor.run_forever(speed_sp=100)
            rightMotor.run_forever(speed_sp=0)
        else:
            print("approaching the object now")
            if(distance <= 20):
                rightMotor.stop()
                leftMotor.stop()
                search_object = True
            else:
                driveForever()


'''This method allows the robot to avoid any obstacles on its path as it either
    wanders randomlys or approaches a green object'''
def avoidObstacle():
    global seen_object
    global search_for_object
    global avoid_obstacle
    print("Avoid running")
    us.mode='US-DIST-CM'
    distance = us.value()/10
    print(distance)
    print(camera.mode)
    while avoid:
        if(camera.mode!=4 and distance<=20):
            seen_object = False
            search_for_object = False
            avoid_obstacle = True
            turnRight(90, 100)
            driveStraight(15, 100)
        else:
            search_for_object = True
            avoid_Obstacle = False


''''The main method creates the main thread and other sub-threads of the target
    methods above that should be prompted by the global varables'''
look = Thread(target = spinAndFind)
appr = Thread(target = approachObject)
avoid = Thread(target = avoidObstacle)
def main():
    setCameraMode(4)
    while (not button.any()):
                
        
main()
