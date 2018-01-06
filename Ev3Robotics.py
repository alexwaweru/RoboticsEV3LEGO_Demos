##!/usr/bin/env python3
import ev3dev.ev3 as ev3
from multiprocessing import Process
import time as t
import math

left_motor = ev3.LargeMotor('outC')
right_motor = ev3.LargeMotor('outB')


def drive_straight_forever(speed = 450):
    left_motor.run_forever(speed_sp=speed )
    right_motor.run_forever(speed_sp=speed)


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


def reverse_straight(distance):
    radius = 2.8 #take measurement
    pi = math.pi
    circumference = 2*pi*radius
    angle = ((distance*360)/circumference)*(-1)
    right_motor.run_to_rel_pos(position_sp=angle, speed_sp=450)
    right_motor.wait_while('running')
    left_motor.run_to_rel_pos(position_sp=angle, speed_sp=450)
    left_motor.wait_while('running')


def reverseRight(angle, speed):
    #Left moto takes the turnLeft
    width = 12.3 #measure width of the robot
    circumference = 2*(math.pi)*width
    distance = (angle/360)*circumference
    wheel_radius = 2.8 #measure radius of wheel_radius
    turn_angle = ((distance*360)/(2*(math.pi)*wheel_radius))*(-1)
    left_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=450)
    left_motor.wait_while('running')


def reverseLeft(angle, speed):
    #Right motor takes the turnLeft
    width = 12.3 #measure width of the robot
    circumference = 2*(math.pi)*width
    distance = (angle/360)*circumference
    wheel_radius = 2.8 #measure radius of wheel_radius
    turn_angle = ((distance*360)/(2*(math.pi)*wheel_radius))*(-1)
    right_motor.run_to_rel_pos(position_sp=turn_angle, speed_sp=450)
    right_motor.wait_while('running')


def test_run():
    drive_straight(100)
    turnRight()
    drive_straight(100)
    turnLeft()
    spin(3600)
    reverse_straight(100)



if __name__ == '__main__':
    test_run()
