#

from machine import Pin

#initialise the keypad,
#rows = input with pull up
#cols = output
def initKeypad(pin_nos):
    keypadPins = []

    tmp = []
    for i in pin_nos[0]:
        tmp.append( Pin(i, Pin.IN, Pin.PULL_UP) )
    keypadPins.append(tmp)

    tmp = []
    for i in pin_nos[1]:
        tmp.append( Pin(i, Pin.OUT) )
    keypadPins.append(tmp)
    
    return keypadPins

######################################################
def scanKeypad(keypadPins):
    for i in keypadPins[1]:
        i.value(1)
    
    for i in range(len(keypadPins[1])):
        keypadPins[1][i].value(0)
        for j in range(len(keypadPins[0])):
            if(keypadPins[0][j].value() == 0):
                return [j,i]
        keypadPins[1][i].value(1)
    return [-1,-1]

keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
    ]
pin_nos = [ [2, 3, 4, 5], [6, 7, 8, 9] ]
keypad = initKeypad(pin_nos)
while True:
    swState = scanKeypad(keypad)
    if(swState != [-1, -1]):
        print(keys[swState[0]][swState[1]])
