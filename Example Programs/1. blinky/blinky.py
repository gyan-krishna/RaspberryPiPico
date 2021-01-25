#blinking built in led

from machine import Pin
from time import sleep

led_builtin = Pin(25, Pin.OUT)

while True:
    led_builtin.toggle()
    sleep(0.5)