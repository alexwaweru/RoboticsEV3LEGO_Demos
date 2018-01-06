#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from time   import sleep
import Ev3Robotics as evr
def main():
    cl = ev3.ColorSensor()
    assert cl.connected, "Connect a single EV3 color sensor to any sensor port"

    # Connect touch sensor to any sensor port and check it is connected.
    ts = ev3.TouchSensor()
    assert ts.connected, "Connect a touch sensor to any port"

    # Put the color sensor into COL-COLOR mode.
    cl.mode='COL-COLOR'

    colors=('unknown','black','blue','green','yellow','red','white','brown')
    evr.drive_straight_forever(500)
    while not ts.value():    # Stop program by pressing touch sensor button
        if colors[cl.value()] == "green":
            evr.turnRight()
        elif colors[cl.value()] == "red":
            evr.turnLeft()
        elif colors[cl.value()] == "black":
            evr.stop()
            Sound.beep()
