#shift register - 74_hc_595

# pin 13 - output enable - EN - GND
# pin 10 - reset - RST - VCC
# pin 13 - LATCH CLOCK - GPIO 3
# pin 11 - SHIFT CLOCK - GPIO 4
# pin 14 - Data in - A - GPIO 2

# pin 8  - GND
# pin 16 - vcc

from machine import Pin
from time import sleep

class ShiftReg:
    def __init__(self, data, latch, shift):
        self.data = Pin(data, Pin.OUT)
        self.latch = Pin(latch, Pin.OUT)
        self.shift = Pin(shift, Pin.OUT)
    def shiftIn(self, data):
        td = 0.001
        mask = 1
        for i in range(8):
            if(mask & data == 0):
                print(0)
                self.data.value(0)
            else:
                print(1)
                self.data.value(1)
                
            sleep(td)
            self.shift.value(1)
            sleep(td)
            self.shift.value(0)
            sleep(td)
            mask = mask << 1
        self.latch.value(1)
        sleep(td)
        self.latch.value(0)

reg = ShiftReg(2, 3, 4)
reg.shiftIn(0b10101010)