#connect a switch to GPIO15 [pin 20] 


from machine import Pin, Timer
from time import sleep

sw = Pin(15, Pin.IN)

while True:
    if(sw.value() == 1):
        print("button pressed")
        sleep(1)