# raspberry pi 2040 has a 12 bit adc - 0 - 4095
# internally the 12bit value is converted to 16bits
# i.e. 0 - 65,535

# Connection :-
# wiper of potentiometer connected to ADC0 [PIN 31].

from time import sleep

sense_in = machine.ADC(26)

#conversion factor to convert adc value to Voltage
k = 3.3/65535 

while(True):
    raw_data = sense_in.read_u16()
    voltage =  raw_data * k
    print("raw data = ", raw_data, "voltage = ", voltage, "V")
    sleep(0.1)