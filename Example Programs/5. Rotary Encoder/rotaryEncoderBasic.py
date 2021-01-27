from machine import Pin
from time import sleep

sw  = Pin(10, Pin.IN)
dt  = Pin(11, Pin.IN)
clk = Pin(12, Pin.IN)

last_CLK_State = clk.value()
counter = 0

while(True):
    current_CLK_State = clk.value()
    if(current_CLK_State != last_CLK_State and current_CLK_State == 1):
        if(dt.value() != current_CLK_State):
            counter+=1
        else:
            counter-=1
        print(counter)
    last_CLK_State = current_CLK_State
    
    if(sw.value() == 0):
        print("button pressed")
        sleep(0.5)