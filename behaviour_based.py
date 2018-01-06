##!/usr/bin/env python3
import ev3dev.ev3 as ev3
from threading import Thread

left_motor = ev3.LargeMotor('outC')
right_motor = ev3.LargeMotor('outB')
lcd = ev3.Screen() 
ts = ev3.TouchSensor('in2');    assert ts.connected, "Connect a touch sensor to any port" 
us = ev3.UltrasonicSensor() 
us.mode='US-DIST-CM'
units = us.units # reports 'cm' even though the sensor measures 'mm'

def stop():
    left_motor.stop()
    right_motor.stop() 

def drive_straight(distance):
    radius = 2.8#take measurement
    pi = math.pi
    circumference = 2*pi*radius
    angle = (distance*360)/circumference
    left_motor.run_to_rel_pos(position_sp=angle, speed_sp=450 )
    right_motor.run_to_rel_pos(position_sp=angle, speed_sp=450)
    right_motor.wait_while('running')
    left_motor.wait_while('running')

def spin(angle = 360, speed=450):
    left_motor.run_to_rel_pos(position_sp=angle, speed_sp=450)
    left_motor.run_to_rel_pos(position_sp= (-1)*angle, speed_sp=450)

def turnRight(angle=90, speed=10):
    #Left moto takes the turnLeft
    width = 12.3 #measure width of the robot
    circumference = 2*(math.pi)*width
    distance = (angle/360)*circumference
    wheel_radius = 2.8 #measure radius of wheel_radius
    turn_angle = (distance*360)/(2*(math.pi)*wheel_radius)
    left_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=450)
    left_motor.wait_while('running')

def turnLeft(angle=90, speed=450):
    #Right motor takes the turnLeft
    width = 12.3 #measure width of the robot
    circumference = 2*(math.pi)*width
    distance = (angle/360)*circumference
    wheel_radius = 2.8 #measure radius of wheel_radius
    turn_angle = (distance*360)/(2*(math.pi)*wheel_radius)
    right_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=450)
    right_motor.wait_while('running')

def setCameraMode(sigNum):
	camera.mode = 'SIG'+str(sigNum) 

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
    if  objCount < 0:  
        turnRight()
        drive_straight(50)
    else:
        stop()

def look():
    while not ts.value():    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
    distance = us.value()/10  # convert mm to cm    
    print(str(distance) + " " + units)
    print(str(error) + " " + units)
    lcd.draw.text((10,10), str(distance)+ " " + units)
    lcd.draw.text((10,10), str(error)+ " " + units)

    objCount = camera.value(0)	# get the number of objects seen by the camera
    if objCount < 0:  #This is an inconveniently large distance
        turnRight()
    elif(objCount > 0): # if we've seen at least one object 
        stop()
    else:
        leftMotor.run_forever()
        rightMotor.run_forever()

def approach():
  separation = 20
  constant = 50
  while not ts.value():    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
    distance = us.value()/10  # convert mm to cm
    error = distance - separation      
    print(str(distance) + " " + units)
    print(str(error) + " " + units)
    lcd.draw.text((10,10), str(distance)+ " " + units)
    lcd.draw.text((10,10), str(error)+ " " + units)

    if distance > separation :  #This is an inconveniently large distance
      output = constant * error + 0 
      if(output > 1000):
        output = 990
      else:
        output = constant * error + 0 
        left_motor.run_forever(speed_sp=output)
        right_motor.run_forever(speed_sp=output)
    else:
        Sound.tone(1000, 200).wait()  #1000Hz for 0.2s
        sleep(0.5)

def main():
    look_for_object = Thread(target = look)
    approach_green_object = Thread(target = approach)
    avoid_nongreen_objects = Thread(target = avoid)

    

    
