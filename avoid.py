#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

lcd = ev3.Screen()                   # The EV3 display
rightMotor = ev3.LargeMotor('outB')  # The motor connected to the right wheel
leftMotor = ev3.LargeMotor('outC')   # The motor connected to the left wheel
button = ev3.Button()				 # Any button
camera = ev3.Sensor(address=ev3.INPUT_1)	 # The camera
assert camera.connected, "Error while connecting Pixy camera to port 2"

lcd = ev3.Screen()
ts = ev3.TouchSensor('in2');    assert ts.connected, "Connect a touch sensor to any port" 
us = ev3.UltrasonicSensor() 
us.mode='US-DIST-CM'
units = us.units
# reports 'cm' even though the sensor measures 'mm'

CAMERA_WIDTH_PIXELS = 255
CAMERA_HEIGHT_PIXELS = 255

leftMotor = ev3.LargeMotor('outC')
rightMotor = ev3.LargeMotor('outB')
lcd = ev3.Screen()

ts = ev3.TouchSensor('in2');    assert ts.connected, "Connect a touch sensor to any port" 
us = ev3.UltrasonicSensor() 

us.mode='US-DIST-CM'

units = us.units
# reports 'cm' even though the sensor measures 'mm'

def stop():
    leftMotor.stop()
    rightMotor.stop()

def turnLeft(angle=90, speed=10):
    #Left moto takes the turnLeft
    width = 12.3 #measure width of the robot
    circumference = 2*(math.pi)*width
    distance = (angle/360)*circumference
    wheel_radius = 2.8 #measure radius of wheel_radius
    turn_angle = (distance*360)/(2*(math.pi)*wheel_radius)
    left_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=450)
    left_motor.wait_while('running')
    
def turnRight(angle=90, speed=450):
    #Right motor takes the turnLeft
    width = 12.3 #measure width of the robot
    circumference = 2*(math.pi)*width
    distance = (angle/360)*circumference
    wheel_radius = 2.8 #measure radius of wheel_radius
    turn_angle = (distance*360)/(2*(math.pi)*wheel_radius)
    right_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=450)
    right_motor.wait_while('running')

def drive_straight(distance):
    radius = 2.8#take measurement
    pi = math.pi
    circumference = 2*pi*radius
    angle = (distance*360)/circumference
    left_motor.run_to_rel_pos(position_sp=angle, speed_sp=450 )
    right_motor.run_to_rel_pos(position_sp=angle, speed_sp=450)
    right_motor.wait_while('running')
    left_motor.wait_while('running')
 
def avoid():
  while not ts.value():    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
    distance = us.value()/10  # convert mm to cm
    error = distance - separation      
    print(str(distance) + " " + units)
    print(str(error) + " " + units)
    lcd.draw.text((10,10), str(distance)+ " " + units)
    lcd.draw.text((10,10), str(error)+ " " + units)

    objCount = camera.value(0)	# get the number of objects seen by the camera

    if distance < 20 and objCount < 0:  #This is an inconveniently large distance
        turnRight()
        drive_straight(50)
    else:
        stop()

def setCameraMode(sigNum):
	camera.mode = 'SIG'+str(sigNum)   
          
def main():
  setCameraMode(5)
  while (not button.any()):
    avoid()
    # Add a delay to reduce frequency of printing info to screen
    time.sleep(2)
   
if __name__ == '__main__':
  main()
