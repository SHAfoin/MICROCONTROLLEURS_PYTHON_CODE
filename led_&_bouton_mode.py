from time import sleep, time

import board
from digitalio import DigitalInOut, Direction
# GP14
led = DigitalInOut(board.GP14)
led.direction = Direction.OUTPUT

bouton = DigitalInOut(board.GP13)
bouton.direction = Direction.INPUT

mode = 0
led.value = False
boutonPressed = False

while True :
    
    if bouton.value and not boutonPressed:
        mode = mode + 1 % 4
        boutonPressed = True
    elif not bouton.value:
        boutonPressed = False
    
    if mode == 0:
        led.value = False
    elif mode == 1:
        led.value = True
    elif mode == 2:
        led.value = not led.value
        sleep(1)
        led.value = not led.value
    elif mode == 3:
        led.value = not led.value
        sleep(0.2)
        led.value = not led.value
    else:
        mode = 0
            
    sleep(0.1)