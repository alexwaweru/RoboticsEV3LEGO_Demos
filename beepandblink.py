#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from threading import Thread
lcd = Screen()                   # The EV3 display

global beep
global blink
global exit

beep = False
blink = False
exit = False

def playtone():
    global beep
    global exit
    while not exit:             
        if beep == True:
          Sound.tone(1000, 200).wait()  
          sleep(0.5)
          
        
def blinkLight():
    global blink
    global exit
    on = True
    while not exit:            
        if blink == True:
          if on == True:
            lcd.draw.rectangle((0,0,177,80), fill='black')
          else:
            lcd.draw.rectangle((0,0,177,80), fill='white')
          lcd.update()
          sleep(0.5)
          on = not on
        else:
          lcd.clear() 
          

          
t1 = Thread(target=playtone)
t1.start()
t2 = Thread(target=blinkLight)
t2.start()

def main():
  global beep
  global blink
  global exit

  while (not exit):
    msg = input("Enter command: ")
    if msg == "blinkOn":
      print("Starting blinking")
      blink = True
    elif msg == "blinkOff":
      print("Stopping blinking")
      blink = False
    elif msg == "beepOn":
      print("Starting beeping")
      beep = True
    elif msg == "beepOff":
      print("Stopping beeping")
      beep = False
    elif msg == "exit":
      print("Exiting")
      exit = True
      
      
main()
      
  
